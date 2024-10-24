from fuzzylogic.classes import Domain
from fuzzylogic.functions import gauss, sigmoid

def heat_membership():
    # Define the domain (universe of discourse) for heat: 0°C to 60°C
    heat = Domain("Heat", 0, 60, res=0.1)

    # Define Gaussian membership functions for the heat levels
    heat.normal = sigmoid(1, -1, 15)
    heat.hazardous = gauss(c=25, b=0.05, c_m=1)
    heat.caution = gauss(c=32, b=0.25, c_m=1)
    heat.danger = sigmoid(1, 1, 35)

    return heat

def precipitation_membership():
    precipitation = Domain("Precipitation", 0, 15, res=0.1)

    precipitation.light = sigmoid(1, -2, 2.5)
    precipitation.moderate = gauss(c=5, b=0.2, c_m=1)
    precipitation.heavy = sigmoid(1, 2, 7)

    return precipitation

def flood_risk_membership():
    flood_risk = Domain("Flood Risk", 0, 2, res=0.1)

    flood_risk.low = sigmoid(1, -10, 0.5)
    flood_risk.medium = gauss(c=1, b=10, c_m=1)
    flood_risk.high = sigmoid(1, 10, 1.5)

    return flood_risk
