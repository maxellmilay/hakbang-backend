from rest_framework import serializers
from annotation.models import File, Location, AnnotationForm, Annotation, AnnotationImage, Coordinates


class FileSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = File
        fields = '__all__'


class CoordinatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coordinates
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    start_coordinates = CoordinatesSerializer(read_only=True)
    end_coordinates = CoordinatesSerializer(read_only=True)
    start_coordinates_id = serializers.IntegerField(write_only=True)
    end_coordinates_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Location
        fields = '__all__'


class AnnotationFormSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    updated_on = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = AnnotationForm
        fields = '__all__'


class Annotation(serializers.ModelSerializer):
    location = LocationSerializer()
    annotator = serializers.CharField(source='annotator.username')
    form_template = AnnotationFormSerializer()
    created_on = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    updated_on = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = Annotation
        fields = '__all__'