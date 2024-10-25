from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError

from annotation.models import Annotation, Location

import pickle
import json

from annotation.utils.accessibility_score import calculate_accessibility_score
from annotation.utils.weather import get_weather_data

class Command(BaseCommand):
    help = 'Test Model Integration'

    def handle(self, *args, **options):
        try:
            location = Location.objects.get(id=326)

            with open('models/nn_model.pkl', 'rb') as file:
                model = pickle.load(file)

            anchored_weather_data = {}

            coordinates = location.anchor.split(',')
            longitude = float(coordinates[0])
            latitude = float(coordinates[1])
            weather_data = get_weather_data(latitude, longitude)
            anchored_weather_data[location.anchor] = weather_data

            annotation = location.annotations.all()

            annotation_data = annotation.first().form_data
            annotation_data = json.loads(annotation_data)

            data = calculate_accessibility_score(location, model, anchored_weather_data, Annotation, annotation_data)

            print('ACCESSIBILITY: ',data['accessibility_probability'])
            print('ACCESSIBILITY: ',data['results'])

            location.accessibility_score = data['accessibility_probability']
            location.results = data['results']

            self.stdout.write(self.style.SUCCESS(f'Successfully saved accessibility score'))
        except ValidationError as e:
            self.stdout.write(self.style.ERROR(f'ValidationError: {e}'))
