from django.shortcuts import render
from .serializers import LocationSerializer, AnnotationFormSerializer
from .models import Location, AnnotationForm
from main.utils.generic_api import GenericView


class LocationView(GenericView):
    queryset = Location.objects.filter(removed=False)
    serializer_class = LocationSerializer


class AnnotationFormView(GenericView):
    queryset = AnnotationForm.objects.filter(removed=False)
    serializer_class = AnnotationFormSerializer