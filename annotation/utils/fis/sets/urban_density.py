from fuzzylogic.classes import Domain
from fuzzylogic.functions import gauss, sigmoid

def key_areas_membership():
    key_areas = Domain("Key Areas", 0, 200, res=0.1)

    key_areas.few = sigmoid(L=1, k=-0.05, x0=40)        # Rising sigmoid centered at 40
    key_areas.moderate = gauss(c=80, b=0.0025, c_m=1)   # Gaussian centered at 80
    key_areas.many = sigmoid(L=1, k=0.05, x0=120)       # Falling sigmoid centered at 120

    return key_areas

def population_membership():
    # Define the domain (universe of discourse) for population (0-25)
    population = Domain("Population", 0, 25, res=0.1)

    # Define sigmoid functions for "very_low" and "very_high"
    population.very_low = sigmoid(L=1, k=-1.0, x0=4)      # Rising sigmoid centered at 4
    population.low = gauss(c=8, b=0.25, c_m=1)            # Gaussian centered at 8
    population.moderate = gauss(c=12, b=0.25, c_m=1)      # Gaussian centered at 12
    population.high = gauss(c=16, b=0.25, c_m=1)          # Gaussian centered at 16
    population.very_high = sigmoid(L=1, k=1.0, x0=20)     # Falling sigmoid centered at 20

    return population
