from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError

from annotation.utils.neural_network.predict import predict
from annotation.utils.fis.fis import FuzzyInferenceSystem

class Command(BaseCommand):
    help = 'Test Model Integration'

    def handle(self, *args, **options):
        try:
            input = {
                'flood_risk': 0,
                'heat_index': 50,
                'precipitation': 1,
                'key_areas': 25,
                'population': 5,
                'walkway_width': 0.05,
                'zone_area': 1,
                'gradient': 1,
                'surface': 0.001,
                'street_furniture': 1,
                'border_buffer': 1,
                'lighting': 3
            }

            fis = FuzzyInferenceSystem(input)

            features = {
                'weather_condition': fis.crisp_weather_condition,
                'urban_density': fis.crisp_urban_density,
                'sidewalk_capacity': fis.crisp_sidewalk_capacity,
                'sidewalk_capacity': fis.crisp_sidewalk_capacity,
                'safety_risk': fis.crisp_safety_risk,
                'accessibility': fis.accessibility
            }

            data = [features]

            predicted_accessibility_probability = predict(data)

            self.stdout.write(self.style.SUCCESS(f"Predicted Accessibility: {predicted_accessibility_probability}"))
        except ValidationError as e:
            self.stdout.write(self.style.ERROR(f'ValidationError: {e}'))
