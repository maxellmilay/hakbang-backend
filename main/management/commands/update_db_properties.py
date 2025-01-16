from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
import json
import os

from annotation.models import Coordinates, Sidewalk

class Command(BaseCommand):
    help = 'Populate the database with GeoJSON data from a .json file'

    def add_arguments(self, parser):
        parser.add_argument('geojson_file_path', type=str, help='Path to the GeoJSON file')

    def handle(self, *args, **options):
        geojson_file_path = options['geojson_file_path']

        if not os.path.isfile(geojson_file_path):
            self.stdout.write(self.style.ERROR(f'File not found: {geojson_file_path}'))
            return

        # Use parse_float=str to read numbers as strings, preserving precision
        with open(geojson_file_path, 'r') as f:
            data = json.load(f, parse_float=str)

        for feature in data.get('features', []):
            properties = feature.get('properties', {})
            geometry = feature.get('geometry', {})
            coordinates = geometry.get('coordinates', [])

            # Ensure it's a LineString with exactly 2 points
            if geometry.get('type') != 'LineString' or len(coordinates) != 2:
                self.stdout.write(self.style.ERROR('Each feature must be a LineString with exactly 2 coordinates.'))
                continue

            # Get start and end coordinates as strings
            start_coord = coordinates[0]
            end_coord = coordinates[1]

            # Extract latitude and longitude as strings
            start_longitude = start_coord[0]  # Already a string due to parse_float=str
            start_latitude = start_coord[1]
            end_longitude = end_coord[0]
            end_latitude = end_coord[1]

            # Get Coordinates objects with latitude and longitude as strings
            start_coordinates = Coordinates.objects.get(
                latitude=start_latitude,
                longitude=start_longitude,
                removed=False
            )

            end_coordinates = Coordinates.objects.get(
                latitude=end_latitude,
                longitude=end_longitude,
                removed=False
            )

            # Get Sidewalk
            sidewalk = Sidewalk.objects.get(
                start_coordinates=start_coordinates,
                end_coordinates=end_coordinates
            )

            if sidewalk:

                sidewalk.data = properties

                try:
                    sidewalk.full_clean()
                    sidewalk.save()
                    self.stdout.write(self.style.SUCCESS(f'Successfully updated sidewalk with id {sidewalk.id}'))
                except ValidationError as e:
                    self.stdout.write(self.style.ERROR(f'ValidationError: {e}'))
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'Sidewalk from {start_coordinates} to {end_coordinates} already exists. Skipping.'
                    )
                )
