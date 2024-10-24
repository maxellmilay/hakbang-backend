from annotation.utils.fis.fuzzy_logic import fuzzy_AND, fuzzy_OR

# Bad condition: Severe combinations of flood hazard, precipitation, and heat.
def bad_weather_condition(f, h, p, flood_hazard, heat, precipitation):
    return fuzzy_OR(
        # HIGH FLOOD HAZARD
        fuzzy_AND(flood_hazard.high(f), precipitation.heavy(p)),
        fuzzy_AND(flood_hazard.high(f), precipitation.moderate(p)),
        fuzzy_AND(flood_hazard.high(f), precipitation.light(p)),

        fuzzy_AND(flood_hazard.high(f), precipitation.light(p), heat.danger(h)),
        fuzzy_AND(flood_hazard.high(f), precipitation.light(p), heat.caution(h)),

        # MODERATE FLOOD HAZARD
        fuzzy_AND(flood_hazard.medium(f), precipitation.heavy(p)),
        fuzzy_AND(flood_hazard.medium(f), precipitation.moderate(p)),

        fuzzy_AND(flood_hazard.medium(f), precipitation.light(p), heat.danger(h)),
        fuzzy_AND(flood_hazard.medium(f), precipitation.light(p), heat.caution(h)),

        # LOW FLOOD HAZARD
        fuzzy_AND(flood_hazard.low(f), precipitation.heavy(p)),

        fuzzy_AND(flood_hazard.low(f), precipitation.light(p), heat.danger(h)),
        fuzzy_AND(flood_hazard.low(f), precipitation.light(p), heat.caution(h))
    )


# Moderate condition: Intermediate risk with some caution needed.
def moderate_weather_condition(f, h, p, flood_hazard, heat, precipitation):
    return fuzzy_OR(
        # HIGH FLOOD HAZARD
        fuzzy_AND(flood_hazard.high(f), precipitation.light(p), heat.hazardous(h)),

        # MODERATE FLOOD HAZARD
        fuzzy_AND(flood_hazard.medium(f), precipitation.light(p), heat.hazardous(h)),
        fuzzy_AND(flood_hazard.medium(f), precipitation.moderate(p)),

        # LOW FLOOD HAZARD
        fuzzy_AND(flood_hazard.low(f), precipitation.light(p), heat.hazardous(h)),
        fuzzy_AND(flood_hazard.low(f), precipitation.moderate(p))
    )


# Good condition: Favorable combinations for normal activity.
def good_weather_condition(f, h, p, flood_hazard, heat, precipitation):
    return fuzzy_OR(
        # HIGH FLOOD HAZARD
        fuzzy_AND(flood_hazard.high(f), precipitation.light(p), heat.normal(h)),

        # MODERATE FLOOD HAZARD
        fuzzy_AND(flood_hazard.medium(f), precipitation.light(p), heat.normal(h)),

        # LOW FLOOD HAZARD
        fuzzy_AND(flood_hazard.low(f), precipitation.moderate(p)),
        fuzzy_AND(flood_hazard.low(f), precipitation.light(p), heat.normal(h))
    )
