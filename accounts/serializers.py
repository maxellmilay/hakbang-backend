from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from accounts.models import CustomUser, Organization

from annotation.serializers import FileSerializer


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
    profile_picture = FileSerializer(read_only=True)
    profile_picture_id = serializers.IntegerField(write_only=True, required=False)
    organization = OrganizationSerializer(read_only=True)
    organization_id = serializers.IntegerField(write_only=True, required=False)

    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'full_name', 'is_admin', 'profile_picture', 'profile_picture_id', 'organization', 'organization_id']
        read_only_fields = ['id', 'is_admin']

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['user'] = UserSerializer(self.user).data
        return data