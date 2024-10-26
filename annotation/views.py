from .base_serializers import LocationSerializer, AnnotationFormSerializer, AnnotationImageSerializer, FileSerializer
from .serializers.annotation import AnnotationSerializer, SidebarAnnotationsSerializer, AnnotationNameCheckerSerializer
from .models import Location, AnnotationForm, Annotation, AnnotationImage, File
from main.utils.generic_api import GenericView
from annotation.utils.accessibility_score import individual_update_accessibility_scores

from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

import json

class LocationView(GenericView):
    queryset = Location.objects.filter(removed=False).order_by('accessibility_score')
    serializer_class = LocationSerializer
    size_per_request = 20


class AnnotationFormView(GenericView):
    queryset = AnnotationForm.objects.filter(removed=False)
    serializer_class = AnnotationFormSerializer


class AnnotationView(GenericView):
    queryset = Annotation.objects.filter(removed=False)
    serializer_class = AnnotationSerializer

    @transaction.atomic
    def create(self, request):
        if 'create' not in self.allowed_methods:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        location_id = request.data.get('location_id')
        start_coordinates_id = Location.objects.get(id=location_id).start_coordinates_id
        request.data['coordinates_id'] = start_coordinates_id

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            self.cache_object(serializer.data, instance.pk)
            self.invalidate_list_cache()

            location = Location.objects.get(id=instance.location_id)
            
            annotation_data = request.data['form_data']
            annotation_data = json.loads(annotation_data)

            individual_update_accessibility_scores(location, Annotation, annotation_data)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @transaction.atomic
    def update(self, request, pk=None):
        if 'update' not in self.allowed_methods:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        instance = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            self.cache_object(serializer.data, pk)
            self.invalidate_list_cache()

            location = Location.objects.get(id=instance.location_id)

            annotation_data = request.data['form_data']
            annotation_data = json.loads(annotation_data)

            individual_update_accessibility_scores(location, Annotation, annotation_data)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def destroy(self, request, pk=None):
        if 'delete' not in self.allowed_methods:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        instance = get_object_or_404(self.queryset, pk=pk)
        self.delete_cache(pk)
        self.invalidate_list_cache()

        location = Location.objects.get(id=instance.location_id)
        location.accessibility_score = None
        location.save(update_fields=['accessibility_score'])

        if hasattr(instance, 'removed'):
            instance.removed = True
            instance.save(update_fields=['removed'])
        else:
            instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SidebarAnnotationsView(GenericView):
    queryset = Annotation.objects.filter(removed=False).order_by('-updated_on')
    serializer_class = SidebarAnnotationsSerializer
    filter_fields = ['annotator_id']
    allowed_methods = ['list']


class AnnotationNameCheckerView(GenericView):
    queryset = Annotation.objects.filter(removed=False)
    serializer_class = AnnotationNameCheckerSerializer
    filter_fields = ['name']
    allowed_methods = ['list']


class AnnotationImageView(GenericView):
    queryset = AnnotationImage.objects.all()
    serializer_class = AnnotationImageSerializer
    filter_fields = ['annotation_id']


class FileView(GenericView):
    queryset = File.objects.filter(removed=False)
    serializer_class = FileSerializer
    allowed_methods = ['create', 'delete']
