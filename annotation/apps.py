from django.apps import AppConfig
import threading
from annotation.utils import calculate_accessibility_score


class AnnotationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'annotation'

    def ready(self):
        thread = threading.Thread(target=calculate_accessibility_score, daemon=True)
        thread.start()
