import time
import json
import pickle
import numpy as np
from decimal import Decimal

from django.core.exceptions import ValidationError

from annotation.utils.weather import get_weather_data
from annotation.utils.fis.fis import FuzzyInferenceSystem
from annotation.utils.logreg.predict import get_logreg_probabilities
from annotation.utils.neural_network.predict import predict
from annotation.utils.time import get_current_army_hour

NN = 'neural_network'
LOGREG = 'logistic_regression'

def scheduled_recalculate():
    from annotation.models import Location
    from annotation.models import Annotation

    while True:
        print("\nCalculating accessibility score...")

        locations = Location.objects.filter(accessibility_score__isnull=False)

        model_type = NN

        batch_update_accessibility_scores(locations, Annotation, model_type)

        time.sleep(60*30)

def batch_update_accessibility_scores(locations, Annotation, model_type):
    from annotation.models import Location

    with open('models/logistic_regression_model.pkl', 'rb') as file:
        model = pickle.load(file)

    anchored_weather_data = {}

    for coordinates_string, _ in Location.ANCHOR_CHOICES:
        coordinates = coordinates_string.split(',')
        longitude = float(coordinates[0])
        latitude = float(coordinates[1])
        weather_data = get_weather_data(latitude, longitude)
        anchored_weather_data[coordinates_string] = weather_data

    for location in locations:
        data = calculate_accessibility_score(location, model, anchored_weather_data, Annotation, model_type)

        location.accessibility_score = data['accessibility_probability']
        location.results = data['results']

        try:
            location.full_clean()
            location.save()
            print(f"Accessibility for Location {location.id} successfully calculated")
        except ValidationError as e:
            print('ERROR: ', e)

def individual_update_accessibility_scores(location, Annotation, model_type, annotation_data):
    with open('models/logistic_regression_model.pkl', 'rb') as file:
        model = pickle.load(file)

    anchored_weather_data = {}

    coordinates = location.anchor.split(',')
    longitude = float(coordinates[0])
    latitude = float(coordinates[1])
    weather_data = get_weather_data(latitude, longitude)
    anchored_weather_data[location.anchor] = weather_data

    data = calculate_accessibility_score(location, model, anchored_weather_data, Annotation, model_type, annotation_data)

    location.accessibility_score = data['accessibility_probability']
    location.results = data['results']

    try:
        location.full_clean()
        location.save()
    except ValidationError as e:
        print('ERROR: ',e)

def calculate_accessibility_score(location, model, anchored_weather_data, Annotation, model_type, annotation_data=None):
    if not annotation_data:
        annotation = location.annotations.all()

        if len(annotation) == 0:
            return {
                'accessibility_probability': None,
                'results': None
            }

        annotation_data = annotation.first().form_data
        annotation_data = json.loads(annotation_data)

    if not annotation_data['sidewalkPresence']:
        return {
            'accessibility_probability': 0,
            'results': None
        }

    location_data = location.data

    flood_hazard_index = Annotation.FLOOD_HAZARD[str(location_data['hazard'])]
    weather = anchored_weather_data[location.anchor]

    total_key_areas = sum(location_data['nearPlacesFrequency'].values())
    simplified_population = location_data['population']/1000

    zoning_area_index = Annotation.ZONING_AREA[location_data['zone']]

    border_buffer_index = Annotation.BORDER_BUFFER[annotation_data['borderBuffer']['value']]
    lighting_index = Annotation.LIGHTING_CONDITION[annotation_data['lightingCondition']['value']]
    
    current_hour = get_current_army_hour()

    input = {
        'flood_risk': flood_hazard_index,
        'heat_index': weather['heat_index'],
        'precipitation': weather['precipitation'],
        'key_areas': total_key_areas,
        'population': simplified_population,
        'walkway_width': annotation_data['sidewalkWidth']['value'],
        'zone_area': zoning_area_index,
        'gradient': annotation_data['rampGradient']['value'],
        'surface': annotation_data['sidewalkCondition']['value'],
        'street_furniture': annotation_data['streetFurniture']['value'],
        'border_buffer': border_buffer_index,
        'lighting': lighting_index,
        'time': current_hour
    }
    
    fis = FuzzyInferenceSystem(input)

    crisp_weather_condition = fis.crisp_weather_condition
    crisp_urban_density = fis.crisp_urban_density
    crisp_sidewalk_capacity = fis.crisp_sidewalk_capacity
    crisp_safety_risk = fis.crisp_safety_risk
    raw_accessibility = fis.accessibility

    results = {
        "crisp_weather_condition": crisp_weather_condition,
        "crisp_urban_density": crisp_urban_density,
        "crisp_sidewalk_capacity": crisp_sidewalk_capacity,
        "crisp_safety_risk": crisp_safety_risk,
        "raw_accessibility": raw_accessibility
    }

    converted_results = {k: (int(v) if isinstance(v, np.int64) else float(v) if isinstance(v, np.float64) else v) for k, v in results.items()}
    converted_results = json.dumps(converted_results)

    if model_type == NN:
        accessibility_probability = get_accessibility_probability_from_nn(results)
    elif model_type == LOGREG:
        accessibility_probability = get_accessibility_probability_from_logreg(model, results)
    else:
        accessibility_probability = get_accessibility_probability_from_logreg(model, results)

    return {
        'accessibility_probability':accessibility_probability,
        'results':converted_results
    }

def get_accessibility_probability_from_logreg(model, data):
    input_data = [[data['crisp_weather_condition'], data['crisp_urban_density'], data['crisp_sidewalk_capacity'], data['crisp_safety_risk']]]

    probabilities = get_logreg_probabilities(model,input_data)

    accessibility_probability = probabilities[0][1]
    accessibility_probability = round(Decimal(accessibility_probability), 2)

    return accessibility_probability

def get_accessibility_probability_from_nn(data):
    input = {
        "weather_condition": data['crisp_weather_condition'],
        "urban_density": data['crisp_urban_density'],
        "sidewalk_capacity": data['crisp_sidewalk_capacity'],
        "safety_risk": data['crisp_safety_risk'],
    }

    data = [input]
    accessibility_probability = predict(data)
    accessibility_probability = round(Decimal(accessibility_probability), 2)

    return accessibility_probability
