from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
import json
import os

from annotation.models import Annotation

class Command(BaseCommand):
    help = 'Populate the database with GeoJSON data from a .json file'

    def add_arguments(self, parser):
        parser.add_argument('geojson_file_path', type=str, help='Path to the GeoJSON file')

    def handle(self):
        try:
            Annotation.objects.all().delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully deleted all annotations'))
        except ValidationError as e:
            self.stdout.write(self.style.ERROR(f'ValidationError: {e}'))
