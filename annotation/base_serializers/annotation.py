from rest_framework import serializers
from annotation.models import Location, AnnotationForm, Annotation, AnnotationImage, Coordinates
# from accounts.serializers import UserSerializer


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


class AnnotationBaseSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)
    location_id = serializers.IntegerField(write_only=True)
    created_on = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    updated_on = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)
    annotator_id = serializers.IntegerField(write_only=True)
    form_template = AnnotationFormSerializer(read_only=True)
    form_template_id = serializers.IntegerField(write_only=True)
    coordinates = CoordinatesSerializer(read_only=True)
    coordinates_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Annotation
        fields = '__all__'