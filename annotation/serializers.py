from rest_framework import serializers
from annotation.models import File, Location, AnnotationForm, Annotation, AnnotationImage


class FileSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', read_only=True)

    class Meta:
        model = File
        fields = '__all__'
