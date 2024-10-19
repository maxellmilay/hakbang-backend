from annotation.base_serializers.annotation import AnnotationBaseSerializer
from accounts.serializers import UserSerializer


class AnnotationSerializer(AnnotationBaseSerializer):
    annotator = UserSerializer(read_only=True)

    class Meta:
        model = AnnotationBaseSerializer.Meta.model
        fields = '__all__'
