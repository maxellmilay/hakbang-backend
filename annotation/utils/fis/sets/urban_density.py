from fuzzylogic.classes import Domain
from fuzzylogic.functions import gauss

def key_areas_membership():
    key_areas = Domain("Key Areas", 0, 200, res=0.1)

    # Define Gaussian membership functions for the categories: few, moderate, many
    key_areas.few = gauss(c=40, b=0.0025, c_m=1)       # Centered at 50
    key_areas.moderate = gauss(c=80, b=0.0025, c_m=1)  # Centered at 100
    key_areas.many = gauss(c=120, b=0.001, c_m=1)      # Centered at 150

    return key_areas

def population_membership():
    # Define the domain (universe of discourse) for population (0-25)
    population = Domain("Population", 0, 25, res=0.1)

    # Define Gaussian membership functions for the categories
    population.very_low = gauss(c=4, b=0.25, c_m=1)      # Centered at 4
    population.low = gauss(c=8, b=0.25, c_m=1)           # Centered at 8
    population.moderate = gauss(c=12, b=0.25, c_m=1)     # Centered at 12
    population.high = gauss(c=16, b=0.25, c_m=1)         # Centered at 16
    population.very_high = gauss(c=20, b=0.25, c_m=1)    # Centered at 20

    return population
