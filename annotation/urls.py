from django.urls import path
from .views import LocationView, AnnotationFormView

urlpatterns = [
    path('locations/', LocationView.as_view({'get': 'list', 'post': 'create'}), name='locations'),
    path('locations/<int:pk>/', LocationView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='location'),
    path('annotation-forms/', AnnotationFormView.as_view({'get': 'list', 'post': 'create'}), name='annotation_forms'),
    path('annotation-forms/<int:pk>/', AnnotationFormView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='annotation_form'),
]