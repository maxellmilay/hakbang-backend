from django.apps import AppConfig
import threading
import os
from annotation.utils import update_accessibility_scores

class AnnotationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'annotation'
    thread_started = False

    def ready(self):
        # Only run the thread in the main process, not in autoreload processes
        if os.environ.get('RUN_MAIN') and not self.thread_started:
            self.thread_started = True
            thread = threading.Thread(target=update_accessibility_scores, daemon=True)
            thread.start()
