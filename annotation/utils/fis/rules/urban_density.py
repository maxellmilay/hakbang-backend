from annotation.utils.fis.fuzzy_logic import fuzzy_AND, fuzzy_OR

def low_urban_density(a, p, key_areas, population):
    return fuzzy_OR(
        # Few key areas
        fuzzy_AND(key_areas.few(a), population.very_low(p)),
        fuzzy_AND(key_areas.few(a), population.low(p)),
        fuzzy_AND(key_areas.few(a), population.moderate(p)),

        # Moderate key areas
        fuzzy_AND(key_areas.moderate(a), population.very_low(p)),
        fuzzy_AND(key_areas.moderate(a), population.low(p)),

        # Many key areas
        # no case for that
    )


def moderate_urban_density(a, p, key_areas, population):
    return fuzzy_OR(
        # Few key areas
        fuzzy_AND(key_areas.few(a), population.high(p)),
        fuzzy_AND(key_areas.few(a), population.very_high(p)),

        # Moderate key areas
        fuzzy_AND(key_areas.moderate(a), population.moderate(p)),

        # Many key areas
        # no case for that
    )


def high_urban_density(a, p, key_areas, population):
    return fuzzy_OR(
        # Few key areas
        # no case for that

        # Moderate key areas
        fuzzy_AND(key_areas.moderate(a), population.high(p)),
        fuzzy_AND(key_areas.moderate(a), population.very_high(p)),

        # Many key areas
        fuzzy_AND(key_areas.many(a), population.low(p)),
        fuzzy_AND(key_areas.many(a), population.moderate(p)),
        fuzzy_AND(key_areas.many(a), population.high(p)),
        fuzzy_AND(key_areas.many(a), population.very_high(p))
    )
