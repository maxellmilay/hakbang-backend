from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from accounts.models import CustomUser, Organization

from annotation.serializers import FileSerializer
from annotation.models import File


class OrganizationSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    profile_picture = FileSerializer(read_only=True)
    profile_picture_id = serializers.IntegerField(write_only=True, required=False)
    removed = serializers.BooleanField(write_only=True, required=False)

    class Meta:
        model = Organization
        fields = ['id', 'name', 'created_on', 'profile_picture', 'profile_picture_id', 'removed']


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(read_only=True)
    organization = OrganizationSerializer(read_only=True)
    organization_id = serializers.IntegerField(write_only=True, required=False)
    profile_picture = FileSerializer(read_only=True)
    profile_picture_id = serializers.IntegerField(write_only=True, required=False)
    removed = serializers.BooleanField(write_only=True, required=False)
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'is_admin', 'full_name', 'organization', 'organization_id', 'profile_picture', 'profile_picture_id', 'removed')


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    organization_id = serializers.IntegerField(write_only=True, required=False)
    profile_picture_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'is_admin', 'organization_id', 'profile_picture_id')

    def create(self, validated_data):
        organization_id = validated_data.pop('organization_id', None)
        profile_picture_id = validated_data.pop('profile_picture_id', None)
        if organization_id:
            organization = Organization.objects.get(id=organization_id)
        if profile_picture_id:
            profile_picture = File.objects.get(id=profile_picture_id)
        

        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            is_admin=validated_data.get('is_admin', False),
            organization=organization or None,
            profile_picture=profile_picture or None
        )
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username
        return token

    def validate(self, attrs):
        data = super().validate(attrs)

        data['user'] = UserSerializer(self.user).data
        return data