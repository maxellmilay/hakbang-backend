from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
import json
import os

from geopy.distance import distance

from annotation.models import Coordinates, Location

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

            # Get Location
            location = Location.objects.get(
                start_coordinates=start_coordinates,
                end_coordinates=end_coordinates
            )

            anchor_coordinates = []

            for coordinates, _ in Location.ANCHOR_CHOICES:
                coordinates = coordinates.split(',')
                longitude = float(coordinates[0])
                latitude = float(coordinates[1])
                anchor_coordinates.append((latitude,longitude))

            center_longitude = (float(start_coord[0]) + float(end_coord[0])) / 2
            center_latitude = (float(start_coord[1]) + float(end_coord[1])) / 2

            center_coordinates = (center_latitude,center_longitude)

            nearest_latitude, nearest_longitude = min(anchor_coordinates, key=lambda coord: distance(center_coordinates, coord).km)

            if location:
                location.anchor = f"{nearest_longitude},{nearest_latitude}"
                try:
                    location.full_clean()
                    location.save()
                    self.stdout.write(self.style.SUCCESS(f'Successfully updated location with id {location.id}'))
                except ValidationError as e:
                    self.stdout.write(self.style.ERROR(f'ValidationError: {e}'))
            else:
                self.stdout.write(
                    self.style.WARNING(
                        f'Location from {start_coordinates} to {end_coordinates} already exists. Skipping.'
                    )
                )
