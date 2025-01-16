from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError

from annotation.models import Annotation, Sidewalk

class Command(BaseCommand):
    help = 'Reset Annotations'

    def handle(self, *args, **options):
        try:
            Annotation.objects.all().delete()
            sidewalks = Sidewalk.objects.filter(accessibility_score__isnull=False)
            for sidewalk in sidewalks:
                sidewalk.accessibility_score = None
                sidewalk.full_clean()
                sidewalk.save()

            self.stdout.write(self.style.SUCCESS(f'Successfully deleted all annotations'))
        except ValidationError as e:
            self.stdout.write(self.style.ERROR(f'ValidationError: {e}'))
