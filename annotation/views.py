from .base_serializers.annotation import LocationSerializer, AnnotationFormSerializer, AnnotationImageSerializer
from .serializers.annotation import AnnotationSerializer, SidebarAnnotationsSerializer
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


class SidebarAnnotationsView(GenericView):
    queryset = Annotation.objects.filter(removed=False).order_by('-updated_on')
    serializer_class = SidebarAnnotationsSerializer
    filter_fields = ['annotator_id']


class AnnotationImageView(GenericView):
    queryset = Annotation.objects.filter(removed=False)
    serializer_class = AnnotationImageSerializer
    filter_fields = ['annotation_id']
