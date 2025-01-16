from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError

from annotation.models import Annotation, Sidewalk
from annotation.utils.accessibility_score import batch_update_accessibility_scores

class Command(BaseCommand):
    help = 'Calculate All Accessibility Scores'

    def handle(self, *args, **options):
        try:
            sidewalks = Sidewalk.objects.all()
            
            NN = 'neural_network'
            
            model_type = NN

            batch_update_accessibility_scores(sidewalks, Annotation, model_type)

            self.stdout.write(self.style.SUCCESS('Successfully generated accessibility scores'))
        except ValidationError as e:
            self.stdout.write(self.style.ERROR(f'ValidationError: {e}'))
