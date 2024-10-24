from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError

from annotation.models import Annotation, Location
from annotation.utils.accessibility_score import batch_update_accessibility_scores

class Command(BaseCommand):
    help = 'Calculate All Accessibility Scores'

    def handle(self, *args, **options):
        try:
            locations = Location.objects.all()

            batch_update_accessibility_scores(locations, Annotation)

            self.stdout.write(self.style.SUCCESS(f'Successfully generated accessibility scores'))
        except ValidationError as e:
            self.stdout.write(self.style.ERROR(f'ValidationError: {e}'))
