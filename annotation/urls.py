from django.urls import path
from .views import LocationView, AnnotationFormView, AnnotationView, SidebarAnnotationsView, AnnotationImageView, FileView, AnnotationNameCheckerView

urlpatterns = [
    path('locations/', LocationView.as_view({'get': 'list', 'post': 'create'}), name='locations'),
    path('locations/<int:pk>/', LocationView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='location'),
    path('annotation-forms/', AnnotationFormView.as_view({'get': 'list', 'post': 'create'}), name='annotation_forms'),
    path('annotation-forms/<int:pk>/', AnnotationFormView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='annotation_form'),
    path('annotations/', AnnotationView.as_view({'get': 'list', 'post': 'create'}), name='annotation'),
    path('annotations/<int:pk>/', AnnotationView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='annotation'),
    path('side-panel-annotations/', SidebarAnnotationsView.as_view({'get': 'list'}), name='side_panel_annotations'),
    path('annotation-images/', AnnotationImageView.as_view({'get': 'list', 'post': 'create'}), name='annotation_images'),
    path('annotation-images/<int:pk>/', AnnotationImageView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='annotation_image'),
    path('files/', FileView.as_view({'post': 'create'}), name='files'),
    path('files/<int:pk>/', FileView.as_view({'delete': 'destroy'}), name='file'),
    path('annotation-name-checker/', AnnotationNameCheckerView.as_view({'get': 'list'}), name='annotation_name_checker'),
]