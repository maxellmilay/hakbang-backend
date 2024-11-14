import numpy as np
from annotation.utils.fis.fis import FuzzyInferenceSystem

def generate_fis_data(n_samples):
    print('Generating FIS Data...')

    # Generate random values for weather
    f = np.random.choice([0, 1, 2], n_samples)  # Discrete values for f (0, 1, 2)
    h = np.random.uniform(0, 60, n_samples)     # Continuous values for h (0-60)
    p = np.random.uniform(0, 15, n_samples)     # Continuous values for p (0-15)

    # Generate random values for urban density
    ka = np.random.uniform(0, 200, n_samples)
    pop = np.random.uniform(0, 25, n_samples)

    # Generate random vlaues for safety risk
    w = np.random.uniform(0, 3, n_samples)
    z = np.random.uniform(0, 3, n_samples)

    # Generate random values for safety risk
    g = np.random.uniform(0, 12, n_samples)
    s = np.random.uniform(0, 12, n_samples)
    sf = np.random.uniform(0, 3, n_samples)
    bb = np.random.choice([0, 1], n_samples)
    l = np.random.choice([1, 2 ,3], n_samples)
    t= np.random.uniform(0, 24, n_samples)

    data = []

    for i in range(n_samples):
        input = {
            'flood_risk': f[i],
            'heat_index': h[i],
            'precipitation': p[i],
            'key_areas': ka[i],
            'population': pop[i],
            'walkway_width': w[i],
            'zone_area': z[i],
            'gradient': g[i],
            'surface': s[i],
            'street_furniture': sf[i],
            'border_buffer': bb[i],
            'lighting': l[i],
            'time': t[i]
        }

        fis = FuzzyInferenceSystem(input)

        crisp_weather_condition = fis.crisp_weather_condition
        crisp_urban_density = fis.crisp_urban_density
        crisp_sidewalk_capacity = fis.crisp_sidewalk_capacity
        crisp_safety_risk = fis.crisp_safety_risk
        raw_accessibility = fis.accessibility

        data.append({
            'weather_condition': crisp_weather_condition,
            'urban_density': crisp_urban_density,
            'sidewalk_capacity': crisp_sidewalk_capacity,
            'safety_risk': crisp_safety_risk,
            'accessibility': raw_accessibility
        })

    print('FIS Data Generated!')

    return data
