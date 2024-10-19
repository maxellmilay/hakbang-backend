from .base_serializers.annotation import LocationSerializer, AnnotationFormSerializer
from .serializers.annotation import AnnotationSerializer
from .models import Location, AnnotationForm, Annotation
from main.utils.generic_api import GenericView


class LocationView(GenericView):
    queryset = Location.objects.filter(removed=False)
    serializer_class = LocationSerializer


class AnnotationFormView(GenericView):
    queryset = AnnotationForm.objects.filter(removed=False)
    serializer_class = AnnotationFormSerializer


class AnnotationView(GenericView):
    queryset = Annotation.objects.filter(removed=False)
    serializer_class = AnnotationSerializer
