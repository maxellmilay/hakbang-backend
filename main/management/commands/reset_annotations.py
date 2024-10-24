from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError

from annotation.models import Annotation, Location

class Command(BaseCommand):
    help = 'Reset Annotations'

    def handle(self, *args, **options):
        try:
            Annotation.objects.all().delete()
            locations = Location.objects.filter(accessibility_score__isnull=False)
            for location in locations:
                location.accessibility_score = None
                location.full_clean()
                location.save()

            self.stdout.write(self.style.SUCCESS(f'Successfully deleted all annotations'))
        except ValidationError as e:
            self.stdout.write(self.style.ERROR(f'ValidationError: {e}'))
