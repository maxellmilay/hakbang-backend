import numpy as np

from annotation.utils.fis.rules.weather_condition import bad_weather_condition,moderate_weather_condition, good_weather_condition
from annotation.utils.fis.rules.urban_density import low_urban_density,moderate_urban_density, high_urban_density
from annotation.utils.fis.rules.sidewalk_capacity import low_sidewalk_capacity, moderate_sidewalk_capacity, high_sidewalk_capacity
from annotation.utils.fis.rules.safety_risk import low_safety_risk, moderate_safety_risk, high_safety_risk

from annotation.utils.fis.rules.accessibility import accessible, not_accessible
from annotation.utils.fis.utils import calculate_lighting_score

def fuzzy_weather_condition(f, h, p, flood_hazard, heat, precipitation):
  return (bad_weather_condition(f, h, p, flood_hazard, heat, precipitation),
          moderate_weather_condition(f, h, p, flood_hazard, heat, precipitation),
          good_weather_condition(f, h, p, flood_hazard, heat, precipitation))

def fuzzy_urban_density(a, p, key_areas, population):
  return (low_urban_density(a, p, key_areas, population),
          moderate_urban_density(a, p, key_areas, population),
          high_urban_density(a, p, key_areas, population))

def fuzzy_sidewalk_capacity(w, z, walkway_width, zoning_area):
    return (low_sidewalk_capacity(w, z, walkway_width, zoning_area),
            moderate_sidewalk_capacity(w, z, walkway_width, zoning_area),
            high_sidewalk_capacity(w, z, walkway_width, zoning_area))

def fuzzy_safety_risk(g, s, sf, l, bb, t, gradient, surface, street_furniture, lighting, border_buffer, time):
  lighting_score = calculate_lighting_score(l, t, lighting, time)

  return (low_safety_risk(g, s, sf, bb, gradient, surface, street_furniture, lighting_score, border_buffer),
          moderate_safety_risk(g, s, sf, bb, gradient, surface, street_furniture, lighting_score, border_buffer),
          high_safety_risk(g, s, sf, bb, gradient, surface, street_furniture, lighting_score, border_buffer))

def classify(fuzzy_tup):
    arg_max_idx = np.argmax(fuzzy_tup)
    result = np.zeros(shape=(len(fuzzy_tup), ))
    result[arg_max_idx] = 1
    return tuple(result)

def fuzzy_accessibility(weather_condition_tup, urban_density_tup, sidewalk_capacity_tup, safety_level_tup):
    return (accessible(weather_condition_tup, urban_density_tup, sidewalk_capacity_tup, safety_level_tup),
            not_accessible(weather_condition_tup, urban_density_tup, sidewalk_capacity_tup, safety_level_tup))
