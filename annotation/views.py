from .base_serializers import SidewalkSerializer, AnnotationFormSerializer, AnnotationImageSerializer, FileSerializer
from .serializers.annotation import AnnotationSerializer, SidebarAnnotationsSerializer, AnnotationNameCheckerSerializer, SimpleSidewalkSerializer, AnnotationIdSerializer
from .models import Sidewalk, AnnotationForm, Annotation, AnnotationImage, File, Coordinates
from main.utils.generic_api import GenericView
from annotation.utils.accessibility_score import individual_update_accessibility_scores

from django.db import transaction
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

import json

NN = 'neural_network'
LOGREG = 'logistic_regression'

MODEL_TYPE = NN

class SidewalkView(GenericView):
    queryset = Sidewalk.objects.filter(removed=False).order_by('-accessibility_score')
    serializer_class = SidewalkSerializer
    size_per_request = 600
    
    @transaction.atomic
    def create(self, request):
        if 'create' not in self.allowed_methods:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        start_coord = request.data.get('start_coordinates')
        end_coord = request.data.get('end_coordinates')
        
        # Extract latitude and longitude as strings
        start_longitude = start_coord[0]
        start_latitude = start_coord[1]
        end_longitude = end_coord[0]
        end_latitude = end_coord[1]
        
        # Create or get Coordinates objects with latitude and longitude as strings
        start_coordinates, _ = Coordinates.objects.get_or_create(
            latitude=start_latitude,
            longitude=start_longitude,
            defaults={'removed': False}
        )

        end_coordinates, _ = Coordinates.objects.get_or_create(
            latitude=end_latitude,
            longitude=end_longitude,
            defaults={'removed': False}
        )

        # Check if the Sidewalk already exists
        sidewalk_exists = Sidewalk.objects.filter(
            start_coordinates=start_coordinates,
            end_coordinates=end_coordinates
        ).exists()
        
        if not sidewalk_exists:
            # Create Sidewalk object
            sidewalk = Sidewalk(
                accessibility_score=None,
                adjacent_street=request.data.get('adjacentStreet'),
                data=request.data.get('data'),
                start_coordinates=start_coordinates,
                end_coordinates=end_coordinates
            )

            try:
                sidewalk.full_clean()
                sidewalk.save()
                return Response(f'Success', status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response(f'Validation Error: {e}', status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('Sidewalk already exists', status=status.HTTP_409_CONFLICT)
    
class SimpleSidewalkView(SidewalkView):
    serializer_class = SimpleSidewalkSerializer
    
class AnnotationIdView(APIView):
    def get(self, request, pk):
        request_serializer = AnnotationIdSerializer(data={"id":pk})
        
        print('REQUEST DATA', request.data)
        
        if not request_serializer.is_valid():
            return Response(request_serializer.errors, status=400)

        request_data = request_serializer.data
        
        location_id = request_data["id"]
        
        annotations = Annotation.objects.filter(sidewalk__id=location_id)
        
        annotation_ids = [annotation.id for annotation in annotations]
        
        return Response({"annotation_ids": annotation_ids}, status=status.HTTP_200_OK)
        
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
        
        sidewalk_id = request.data.get('sidewalk_id')
        start_coordinates_id = Sidewalk.objects.get(id=sidewalk_id).start_coordinates_id
        request.data['coordinates_id'] = start_coordinates_id

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            self.cache_object(serializer.data, instance.pk)
            self.invalidate_list_cache()

            sidewalk = Sidewalk.objects.get(id=instance.sidewalk_id)
            
            annotation_data = request.data['data']
            annotation_data = json.loads(annotation_data)

            individual_update_accessibility_scores(sidewalk, Annotation, MODEL_TYPE, annotation_data)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @transaction.atomic
    def update(self, request, pk=None):
        if 'update' not in self.allowed_methods:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        instance = get_object_or_404(self.queryset, pk=pk)
        sidewalk_id = request.data.get('sidewalk_id')
        start_coordinates_id = Sidewalk.objects.get(id=sidewalk_id).start_coordinates_id
        request.data['coordinates_id'] = start_coordinates_id
        serializer = self.serializer_class(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            self.cache_object(serializer.data, pk)
            self.invalidate_list_cache()

            sidewalk = Sidewalk.objects.get(id=instance.sidewalk_id)

            annotation_data = request.data['data']
            annotation_data = json.loads(annotation_data)

            individual_update_accessibility_scores(sidewalk, Annotation, MODEL_TYPE, annotation_data)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def destroy(self, request, pk=None):
        if 'delete' not in self.allowed_methods:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        instance = get_object_or_404(self.queryset, pk=pk)
        self.delete_cache(pk)
        self.invalidate_list_cache()

        sidewalk = Sidewalk.objects.get(id=instance.sidewalk_id)
        sidewalk.accessibility_score = None
        sidewalk.save(update_fields=['accessibility_score'])

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
