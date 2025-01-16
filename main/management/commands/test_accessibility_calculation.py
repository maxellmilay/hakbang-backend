from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError

from annotation.models import Annotation, Sidewalk

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
            sidewalk = Sidewalk.objects.get(id=326)

            if sidewalk.accessibility_score:
                print(f'Previous Accessibility Score: {sidewalk.accessibility_score}')

            with open('models/logistic_regression_model.pkl', 'rb') as file:
                model = pickle.load(file)

            anchored_weather_data = {}

            coordinates = sidewalk.anchor.split(',')
            longitude = float(coordinates[0])
            latitude = float(coordinates[1])
            weather_data = get_weather_data(latitude, longitude)
            anchored_weather_data[sidewalk.anchor] = weather_data

            annotation = sidewalk.annotations.all()

            annotation_data = annotation.first().data
            annotation_data = json.loads(annotation_data)

            model_type = NN

            data = calculate_accessibility_score(sidewalk, model, anchored_weather_data, Annotation, model_type, annotation_data)

            sidewalk.accessibility_score = data['accessibility_probability']
            sidewalk.results = data['results']

            self.stdout.write(self.style.SUCCESS(f'Successfully saved accessibility score {data['accessibility_probability']}'))
        except ValidationError as e:
            self.stdout.write(self.style.ERROR(f'ValidationError: {e}'))
