from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError

from annotation.models import Annotation, Location

import pickle
import json

from annotation.utils.accessibility_score import calculate_accessibility_score
from annotation.utils.weather import get_weather_data

NN = 'neural_network'
LOGREG = 'logistic_regression'

class Command(BaseCommand):
    help = 'Test Model Integration'


    def handle(self, *args, **options):
        try:
            location = Location.objects.get(id=326)

            if location.accessibility_score:
                print(f'Previous Accessibility Score: {location.accessibility_score}')

            with open('models/logistic_regression_model.pkl', 'rb') as file:
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

            model_type = NN

            data = calculate_accessibility_score(location, model, anchored_weather_data, Annotation, model_type, annotation_data)

            location.accessibility_score = data['accessibility_probability']
            location.results = data['results']

            self.stdout.write(self.style.SUCCESS(f'Successfully saved accessibility score {data['accessibility_probability']}'))
        except ValidationError as e:
            self.stdout.write(self.style.ERROR(f'ValidationError: {e}'))
