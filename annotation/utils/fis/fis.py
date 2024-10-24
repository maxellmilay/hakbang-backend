import numpy as np

from annotation.utils.fis.sets.weather_condition import heat_membership, precipitation_membership, flood_risk_membership
from annotation.utils.fis.sets.urban_density import key_areas_membership, population_membership
from annotation.utils.fis.sets.sidewalk_capacity import walkway_width_membership, zoning_area_membership
from annotation.utils.fis.sets.safety_risk import gradient_membership, surface_membership, street_furniture_membership, border_buffer_membership, lighting_membership

from annotation.utils.fis.fuzzy_functions import fuzzy_weather_condition, fuzzy_urban_density, fuzzy_sidewalk_capacity, fuzzy_safety_risk, fuzzy_accessibility, classify
from annotation.utils.fis.fuzzy_logic import defuzzify

from types import SimpleNamespace

class FuzzyInferenceSystem():
    def __init__(self, inputs):
        self.setup_memberships()
        self.setup_fuzzy_inputs(inputs)
        self.generate_fuzz()
        self.calculate_fuzzy_values()
    
    def setup_memberships(self):
        self.heat = heat_membership()
        self.precipitation = precipitation_membership()
        self.flood_risk = flood_risk_membership()

        self.key_areas = key_areas_membership()
        self.population = population_membership()

        self.walkway_width = walkway_width_membership()
        self.zoning_area = zoning_area_membership()

        self.gradient = gradient_membership()
        self.surface = surface_membership()
        self.street_furniture = street_furniture_membership()
        self.border_buffer = border_buffer_membership()
        self.lighting = lighting_membership()
    
    def setup_fuzzy_inputs(self, inputs):
        # Generate random values for weather
        self.f = inputs['flood_risk']  # Discrete values for f (0, 1, 2)
        self.h = inputs['heat_index']     # Continuous values for h (0-60)
        self.p = inputs['precipitation']     # Continuous values for p (0-15)

        # Generate random values for urban density
        self.ka = inputs['key_areas']
        self.pop = inputs['population']

        # Generate random vlaues for safety risk
        self.w = inputs['walkway_width']
        self.z = inputs['zone_area']

        # Generate random values for safety risk
        self.g = inputs['gradient']
        self.s = inputs['surface']
        self.sf = inputs['street_furniture']
        self.bb = inputs['border_buffer']
        self.l = inputs['lighting']

    def generate_fuzz(self):
        # Generate fuzzy and defuzzified values for weather condition
        self.fuzz_weather_condition = fuzzy_weather_condition(self.f, self.h, self.p, self.flood_risk, self.heat, self.precipitation)
        self.fuzz_urban_density = fuzzy_urban_density(self.ka, self.pop, self.key_areas, self.population)
        self.fuzz_sidewalk_capacity = fuzzy_sidewalk_capacity(self.w, self.z, self.walkway_width, self.zoning_area)
        self.fuzz_safety_risk = fuzzy_safety_risk(self.g, self.s, self.sf, self.l, self.bb, self.gradient, self.surface, self.street_furniture, self.lighting, self.border_buffer)

    def calculate_fuzzy_values(self):
        # Calculate fuzzy values for each aspect
        bad_weather_condition, moderate_weather_condition, good_weather_condition = self.fuzz_weather_condition
        low_urban_density, moderate_urban_density, high_urban_density = self.fuzz_urban_density
        low_sidewalk_capacity, moderate_sidewalk_capacity, high_sidewalk_capacity = self.fuzz_sidewalk_capacity
        low_safety_risk, moderate_safety_risk, high_safety_risk = self.fuzz_safety_risk

        self.crisp_weather_condition = defuzzify(self.fuzz_weather_condition)
        self.crisp_urban_density = defuzzify(self.fuzz_urban_density)
        self.crisp_sidewalk_capacity = defuzzify(self.fuzz_sidewalk_capacity)
        self.crisp_safety_risk = defuzzify(self.fuzz_safety_risk)

        # Classify accessibility using the fuzzy values
        accessibility = classify(fuzzy_accessibility(
            weather_condition_tup=SimpleNamespace(
                bad=bad_weather_condition,
                moderate=moderate_weather_condition,
                good=good_weather_condition),
            urban_density_tup=SimpleNamespace(
                low=low_urban_density,
                moderate=moderate_urban_density,
                high=high_urban_density),
            sidewalk_capacity_tup=SimpleNamespace(
                low=low_sidewalk_capacity,
                moderate=moderate_sidewalk_capacity,
                high=high_sidewalk_capacity),
            safety_level_tup=SimpleNamespace(
                low=low_safety_risk,
                moderate=moderate_safety_risk,
                high=high_safety_risk)
        )) 

        self.accessibility = np.argmax(accessibility)
