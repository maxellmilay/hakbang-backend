from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.signals import worker_ready

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')

app = Celery('main')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
app.autodiscover_tasks(['annotation.utils'])

@worker_ready.connect
def at_start(sender, **kwargs):
    from annotation.utils.accessibility_score import recalculate_scores
    recalculate_scores.apply_async(args=[5]) # change this to 60*60*60 for 1 hour interval
