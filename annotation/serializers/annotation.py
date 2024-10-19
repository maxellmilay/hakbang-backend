from annotation.base_serializers.annotation import AnnotationBaseSerializer
from accounts.serializers import UserSerializer


class AnnotationSerializer(AnnotationBaseSerializer):
    annotator = UserSerializer(read_only=True)

    class Meta:
        model = AnnotationBaseSerializer.Meta.model
        fields = '__all__'


class SidebarAnnotationsSerializer(AnnotationSerializer):
    class Meta:
        model = AnnotationSerializer.Meta.model
        fields = ['id', 'updated_on', 'location', 'name']
