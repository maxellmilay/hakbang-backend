from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError

from annotation.models import Annotation, Location
from annotation.utils.accessibility_score import update_accessibility_scores

class Command(BaseCommand):
    help = 'Calculate Accessibility Scores'

    def handle(self, *args, **options):
        try:
            update_accessibility_scores()

            self.stdout.write(self.style.SUCCESS(f'Successfully generated accessibility scores'))
        except ValidationError as e:
            self.stdout.write(self.style.ERROR(f'ValidationError: {e}'))
