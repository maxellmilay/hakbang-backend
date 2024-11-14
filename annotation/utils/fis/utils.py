from annotation.utils.fis.fuzzy_logic import fuzzy_AND, fuzzy_OR
from types import SimpleNamespace

def bad_lighting_score(l, t, lighting, time):
    t_day, t_night = preprocess_time(t)

    return fuzzy_OR(
        # Night, Poor Lighting
        fuzzy_AND(time.night(t_night), lighting.poor(l))
    )

def moderate_lighting_score(l, t, lighting, time):
    t_day, t_night = preprocess_time(t)

    return fuzzy_OR(
        # Night, Adequate Lighting
        fuzzy_AND(time.night(t_night), lighting.adequate(l))
    )

def good_lighting_score(l, t, lighting, time):
    t_day, t_night = preprocess_time(t)

    return fuzzy_OR(
        # Day, Excellent Lighting
        fuzzy_AND(time.day(t_day), lighting.excellent(l)),
        # Day, Poor Lighting
        fuzzy_AND(time.day(t_day), lighting.poor(l)),
        # Day, Adequate Lighting
        fuzzy_AND(time.day(t_day), lighting.adequate(l)),
        # Night, Excellent Lighting
        fuzzy_AND(time.night(t_night), lighting.excellent(l)),
    )

def calculate_lighting_score(l, t, lighting, time):
    # Compute each score using your defined functions
    bad = bad_lighting_score(l, t, lighting, time)
    moderate = moderate_lighting_score(l, t, lighting, time)
    good = good_lighting_score(l, t, lighting, time)

    # Create an object with dot-accessible attributes
    lighting_score = SimpleNamespace(bad=bad, moderate=moderate, good=good)
    return lighting_score

def preprocess_time(t):
    if t >= 6 and t <= 17:  # 6 am to 5 pm
        t_day = t - 5
        t_night = 0
    elif t >= 18:            # beyond 6 pm
        t_day = 0
        t_night = t - 17
    elif t <= 5:             # before 5 am
        t_day = 0
        t_night = t + 7
    else:                    # 5 am to 6 am
        t_day = t - 5
        t_night = t - 17

    return t_day, t_night
