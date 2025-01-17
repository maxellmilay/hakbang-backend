from annotation.base_serializers.annotation import AnnotationBaseSerializer, SidewalkSerializer
from accounts.serializers import UserSerializer


class AnnotationSerializer(AnnotationBaseSerializer):
    annotator = UserSerializer(read_only=True)

    class Meta:
        model = AnnotationBaseSerializer.Meta.model
        fields = '__all__'


class SimpleSidewalkSerializer(SidewalkSerializer):
    class Meta:
        model = SidewalkSerializer.Meta.model
        fields = ['accessibility_score', 'start_coordinates', 'end_coordinates', 'id']


class SidebarAnnotationsSerializer(AnnotationSerializer):
    location = SimpleSidewalkSerializer(read_only=True)
    class Meta:
        model = AnnotationSerializer.Meta.model
        fields = ['id', 'updated_on', 'location', 'name']


class AnnotationNameCheckerSerializer(AnnotationBaseSerializer):
    class Meta:
        model = AnnotationBaseSerializer.Meta.model
        fields = ['name']
