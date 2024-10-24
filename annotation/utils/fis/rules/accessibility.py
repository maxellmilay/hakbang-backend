from annotation.utils.fis.fuzzy_logic import fuzzy_AND, fuzzy_OR

def accessible (weather_condition,  urban_density, road_capacity, safety_level):
    '''
        Params:
          weather_condition should have three values: good, moderate, bad
          urban_density should have three values: low, moderate, high
          road_capacity should have three values: low, moderate, high
          safety_level should have three values: low, moderate, high

        These values are pre-computed using the sub FIS
    '''

    return fuzzy_OR(
        # WEATHER CONDITION = GOOD

            # URBAN DENSITY = HIGH
                # ROAD CAPACITY = HIGH
        fuzzy_AND(weather_condition.good, urban_density.high, road_capacity.high, safety_level.moderate),
        fuzzy_AND(weather_condition.good, urban_density.high, road_capacity.high, safety_level.high),
                # ROAD CAPACITY = MODERATE
        fuzzy_AND(weather_condition.good, urban_density.high, road_capacity.moderate, safety_level.moderate),
        fuzzy_AND(weather_condition.good, urban_density.high, road_capacity.moderate, safety_level.high),

            # URBAN DENSITY = MODERATE
                # ROAD CAPACITY = HIGH
        fuzzy_AND(weather_condition.good, urban_density.moderate, road_capacity.high, safety_level.moderate),
        fuzzy_AND(weather_condition.good, urban_density.moderate, road_capacity.high, safety_level.high),
                # ROAD CAPACITY = MDOERATE
        fuzzy_AND(weather_condition.good, urban_density.moderate, road_capacity.moderate, safety_level.moderate),
        fuzzy_AND(weather_condition.good, urban_density.moderate, road_capacity.moderate, safety_level.high),

            # URBAN DESNITY = LOW
                # ROAD CAPACITY = HIGH
        fuzzy_AND(weather_condition.good, urban_density.low, road_capacity.high, safety_level.low),
        fuzzy_AND(weather_condition.good, urban_density.low, road_capacity.high, safety_level.moderate),
        fuzzy_AND(weather_condition.good, urban_density.low, road_capacity.high, safety_level.high),
                # ROAD CAPACITY = MODERATE
        fuzzy_AND(weather_condition.good, urban_density.low, road_capacity.moderate, safety_level.moderate),
        fuzzy_AND(weather_condition.good, urban_density.low, road_capacity.moderate, safety_level.high),
                # ROAD CAPACITY = LOW
        fuzzy_AND(weather_condition.good, urban_density.low, road_capacity.low, safety_level.moderate),
        fuzzy_AND(weather_condition.good, urban_density.low, road_capacity.low, safety_level.high),

        # WEATHER CONDITION = MODERATE

            # URBAN DENSITY = HIGH
                # ROAD CAPACITY = HIGH
        fuzzy_AND(weather_condition.moderate, urban_density.high, road_capacity.high, safety_level.high),

            # URBAN DENSITY = MODERATE
                # ROAD CAPACITY = HIGH
        fuzzy_AND(weather_condition.moderate, urban_density.moderate, road_capacity.high, safety_level.moderate),
        fuzzy_AND(weather_condition.moderate, urban_density.moderate, road_capacity.high, safety_level.high),
                # ROAD CAPACITY = MODERATE
        fuzzy_AND(weather_condition.moderate, urban_density.moderate, road_capacity.moderate, safety_level.moderate),
        fuzzy_AND(weather_condition.moderate, urban_density.moderate, road_capacity.moderate, safety_level.high),

            # URBAN DENSITY = LOW
                # ROAD CAPACITY = HIGH
        fuzzy_AND(weather_condition.moderate, urban_density.low, road_capacity.high, safety_level.moderate),
        fuzzy_AND(weather_condition.moderate, urban_density.low, road_capacity.high, safety_level.high),
                # ROAD CAPACITY = MODERATE
        fuzzy_AND(weather_condition.moderate, urban_density.low, road_capacity.moderate, safety_level.moderate),
        fuzzy_AND(weather_condition.moderate, urban_density.low, road_capacity.moderate, safety_level.high),
                # ROAD CAPACITY = LOW
        fuzzy_AND(weather_condition.moderate, urban_density.low, road_capacity.low, safety_level.moderate),
        fuzzy_AND(weather_condition.moderate, urban_density.low, road_capacity.low, safety_level.high),

        # WEATHER CONDITION = BAD

            # URBAN DENSITY = HIGH
                # ROAD CAPACITY = HIGH
        fuzzy_AND(weather_condition.bad, urban_density.high, road_capacity.high, safety_level.high),
                # ROAD CAPACITY = MODERATE
        fuzzy_AND(weather_condition.bad, urban_density.high, road_capacity.moderate, safety_level.high),

            # URBAN DENSITY = MODERATE
                # ROAD CAPACITY = HIGH
        fuzzy_AND(weather_condition.bad, urban_density.moderate, road_capacity.high, safety_level.high),
                # ROAD CAPACITY = MODERATE
        fuzzy_AND(weather_condition.bad, urban_density.moderate, road_capacity.moderate, safety_level.high),

            # URBAN DENSITY = LOW
                # ROAD CAPACITY = HIGH
        fuzzy_AND(weather_condition.bad, urban_density.low, road_capacity.high, safety_level.high),
                # ROAD CAPACITY = MODERATE
        fuzzy_AND(weather_condition.bad, urban_density.low, road_capacity.moderate, safety_level.high)
    )


def not_accessible(weather_condition, urban_density, road_capacity, safety_level):
    return fuzzy_OR(
        # WEATHER CONDITION = GOOD

            # URBAN DENSITY = HIGH
                # ROAD CAPACITY = HIGH
        fuzzy_AND(weather_condition.good, urban_density.high, road_capacity.high, safety_level.low),
                # ROAD CAPACITY = MODERATE
        fuzzy_AND(weather_condition.good, urban_density.high, road_capacity.moderate, safety_level.low),
                # ROAD CAPACITY = LOW
        fuzzy_AND(weather_condition.good, urban_density.high, road_capacity.low, safety_level.low),
        fuzzy_AND(weather_condition.good, urban_density.high, road_capacity.low, safety_level.moderate),
        fuzzy_AND(weather_condition.good, urban_density.high, road_capacity.low, safety_level.high),

            # URBAN DENSITY = MODERATE
                # ROAD CAPACITY = HIGH
        fuzzy_AND(weather_condition.good, urban_density.moderate, road_capacity.high, safety_level.low),
                # ROAD CAPACITY = MODERATE
        fuzzy_AND(weather_condition.good, urban_density.moderate, road_capacity.moderate, safety_level.low),
                # ROAD CAPACITY = LOW
        fuzzy_AND(weather_condition.good, urban_density.moderate, road_capacity.low, safety_level.low),
        fuzzy_AND(weather_condition.good, urban_density.moderate, road_capacity.low, safety_level.moderate),
        fuzzy_AND(weather_condition.good, urban_density.moderate, road_capacity.low, safety_level.high),

            # URBAN DENSITY = LOW
                # ROAD CAPACITY = MODERATE
        fuzzy_AND(weather_condition.good, urban_density.low, road_capacity.moderate, safety_level.low),
                # ROAD CAPACITY = LOW
        fuzzy_AND(weather_condition.good, urban_density.low, road_capacity.low, safety_level.low),

        # WEATHER CONDITION = MODERATE

            # URBAN DENSITY = HIGH
                # ROAD CAPACITY = HIGH
        fuzzy_AND(weather_condition.moderate, urban_density.high, road_capacity.high, safety_level.low),
        fuzzy_AND(weather_condition.moderate, urban_density.high, road_capacity.high, safety_level.moderate),
                # ROAD CAPACITY = MODERATE
        fuzzy_AND(weather_condition.moderate, urban_density.high, road_capacity.moderate, safety_level.low),
        fuzzy_AND(weather_condition.moderate, urban_density.high, road_capacity.moderate, safety_level.moderate),
        fuzzy_AND(weather_condition.moderate, urban_density.high, road_capacity.moderate, safety_level.high),
                # ROAD CAPACITY = LOW
        fuzzy_AND(weather_condition.moderate, urban_density.high, road_capacity.low, safety_level.low),
        fuzzy_AND(weather_condition.moderate, urban_density.high, road_capacity.low, safety_level.moderate),
        fuzzy_AND(weather_condition.moderate, urban_density.high, road_capacity.low, safety_level.high),

            # URBAN DENSITY = MODERATE
                # ROAD CAPACITY = HIGH
        fuzzy_AND(weather_condition.moderate, urban_density.moderate, road_capacity.high, safety_level.low),
                # ROAD CAPACITY = MODERATE
        fuzzy_AND(weather_condition.moderate, urban_density.moderate, road_capacity.moderate, safety_level.low),
                # ROAD CAPACITY = LOW
        fuzzy_AND(weather_condition.moderate, urban_density.moderate, road_capacity.low, safety_level.low),
        fuzzy_AND(weather_condition.moderate, urban_density.moderate, road_capacity.low, safety_level.moderate),
        fuzzy_AND(weather_condition.moderate, urban_density.moderate, road_capacity.low, safety_level.high),

            # URBAN DENSITY = LOW
                # ROAD CAPACITY = HIGH
        fuzzy_AND(weather_condition.moderate, urban_density.low, road_capacity.high, safety_level.low),
                # ROAD CAPACITY = MODERATE
        fuzzy_AND(weather_condition.moderate, urban_density.low, road_capacity.moderate, safety_level.low),
                # ROAD CAPACITY = LOW
        fuzzy_AND(weather_condition.moderate, urban_density.low, road_capacity.low, safety_level.low),

        # WEATHER CONDITION = BAD

            # URBAN DENSITY = HIGH
                # ROAD CAPACITY = HIGH
        fuzzy_AND(weather_condition.bad, urban_density.high, road_capacity.high, safety_level.low),
        fuzzy_AND(weather_condition.bad, urban_density.high, road_capacity.high, safety_level.moderate),
                # ROAD CAPACITY = MODERATE
        fuzzy_AND(weather_condition.bad, urban_density.high, road_capacity.moderate, safety_level.low),
        fuzzy_AND(weather_condition.bad, urban_density.high, road_capacity.moderate, safety_level.moderate),
                # ROAD CAPACITY = LOW
        fuzzy_AND(weather_condition.bad, urban_density.high, road_capacity.low, safety_level.low),
        fuzzy_AND(weather_condition.bad, urban_density.high, road_capacity.low, safety_level.moderate),
        fuzzy_AND(weather_condition.bad, urban_density.high, road_capacity.low, safety_level.high),

            # URBAN DENSITY = MODERATE
                # ROAD CAPACITY = HIGH
        fuzzy_AND(weather_condition.bad, urban_density.moderate, road_capacity.high, safety_level.low),
        fuzzy_AND(weather_condition.bad, urban_density.moderate, road_capacity.high, safety_level.moderate),
                # ROAD CAPACITY = MODERATE
        fuzzy_AND(weather_condition.bad, urban_density.moderate, road_capacity.moderate, safety_level.low),
        fuzzy_AND(weather_condition.bad, urban_density.moderate, road_capacity.moderate, safety_level.moderate),
        fuzzy_AND(weather_condition.bad, urban_density.moderate, road_capacity.moderate, safety_level.high),
                # ROAD CAPACITY = LOW
        fuzzy_AND(weather_condition.bad, urban_density.moderate, road_capacity.low, safety_level.low),
        fuzzy_AND(weather_condition.bad, urban_density.moderate, road_capacity.low, safety_level.moderate),
        fuzzy_AND(weather_condition.bad, urban_density.moderate, road_capacity.low, safety_level.high),

            # URBAN DENSITY = LOW
                # ROAD CAPACITY = HIGH
        fuzzy_AND(weather_condition.bad, urban_density.low, road_capacity.high, safety_level.low),
        fuzzy_AND(weather_condition.bad, urban_density.low, road_capacity.high, safety_level.moderate),
                # ROAD CAPACITY = MODERATE
        fuzzy_AND(weather_condition.bad, urban_density.low, road_capacity.moderate, safety_level.low),
        fuzzy_AND(weather_condition.bad, urban_density.low, road_capacity.moderate, safety_level.moderate),
                # ROAD CAPACITY = LOW
        fuzzy_AND(weather_condition.bad, urban_density.low, road_capacity.low, safety_level.low),
        fuzzy_AND(weather_condition.bad, urban_density.low, road_capacity.low, safety_level.moderate),
        fuzzy_AND(weather_condition.bad, urban_density.low, road_capacity.low, safety_level.high)
    )
