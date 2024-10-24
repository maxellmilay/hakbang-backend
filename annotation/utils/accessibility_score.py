import time
import json
import pickle
import random

from django.core.exceptions import ValidationError

from annotation.utils.weather import get_weather_data
from annotation.utils.fis.fis import FuzzyInferenceSystem
from annotation.utils.logreg.predict import get_probabilities


def update_accessibility_scores():
    from annotation.models import Location
    from annotation.models import Annotation

    while True:
        print("Calculating accessibility score...")

        with open('models/logistic_regression_model.pkl', 'rb') as file:
            model = pickle.load(file)

        anchored_weather_data = {}

        for coordinates_string, _ in Location.ANCHOR_CHOICES:
            coordinates = coordinates_string.split(',')
            longitude = float(coordinates[0])
            latitude = float(coordinates[1])
            weather_data = get_weather_data(latitude, longitude)
            anchored_weather_data[coordinates_string] = weather_data

        # get static data from DB
        locations = Location.objects.all()

        for location in locations:
            data = calculate_accessibility_score(location, model, anchored_weather_data, Annotation)

            location.accessibility_score = data['accessibility_score']
            location.results = data['results']

            try:
                location.full_clean()
                location.save()
            except ValidationError as e:
                print('ERROR: ',e)

        time.sleep(60*60)

def calculate_accessibility_score(location, model, anchored_weather_data, Annotation):
    annotation = location.annotations.all()

    if len(annotation) == 0:
        return {'accessibility_probability':None, 'results':None}

    annotation_data = annotation.first().form_data
    annotation_data = json.loads(annotation_data)

    if not annotation_data['sidewalkPresence']:
        return {'accessibility_probability':0, 'results':None}

    location_data = location.data

    flood_hazard_index = Annotation.FLOOD_HAZARD[str(location_data['hazard'])]

    weather = anchored_weather_data[location.anchor]

    zoning_area_index = Annotation.ZONING_AREA[location_data['zone']]

    border_buffer_index = Annotation.BORDER_BUFFER[annotation_data['borderBuffer']]
    lighting_index = Annotation.LIGHTING_CONDITION[annotation_data['lightingCondition']]

    input = {
        'flood_risk': flood_hazard_index,
        'heat_index': weather['heat_index'],
        'precipitation': weather['precipitation'],
        'key_areas': sum(location_data['nearPlacesFrequency'].values()),
        'population': location_data['population']/1000,
        'walkway_width': annotation_data['sidewalkWidth'],
        'zone_area': zoning_area_index,
        'gradient': annotation_data['rampGradient'],
        'surface': annotation_data['sidewalkCondition'],
        'street_furniture': annotation_data['streetFurniture'],
        'border_buffer': border_buffer_index,
        'lighting': lighting_index
    }
    
    fis = FuzzyInferenceSystem(input)

    crisp_weather_condition = fis.crisp_weather_condition
    crisp_urban_density = fis.crisp_urban_density
    crisp_sidewalk_capacity = fis.crisp_sidewalk_capacity
    crisp_safety_risk = fis.crisp_safety_risk
    raw_accessibility = fis.accessibility

    results = {
        'crisp_weather_condition': crisp_weather_condition,
        'crisp_urban_density': crisp_urban_density,
        'crisp_sidewalk_capacity': crisp_sidewalk_capacity,
        'crisp_safety_risk': crisp_safety_risk,
        'raw_accessibility': raw_accessibility
    }

    input_data = [[crisp_weather_condition,crisp_urban_density,crisp_sidewalk_capacity,crisp_safety_risk]]

    probabilities = get_probabilities(model,input_data)

    accessibility_probability = probabilities[0][1]

    return {'accessibility_probability':accessibility_probability, 'results':results}
