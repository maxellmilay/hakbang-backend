from fuzzylogic.classes import Domain
from fuzzylogic.functions import gauss, sigmoid

def walkway_width_membership():
    walkway_width = Domain("walkway_width", 0, 3, res=0.1)

    walkway_width.narrow = sigmoid(1, -10, 1.4)
    walkway_width.midsize = gauss(c=1.65, b=10, c_m=1)
    walkway_width.wide = sigmoid(1, 15, 1.8)

    return walkway_width

def zoning_area_membership():
    zoning_area = Domain("zoning_area", 0, 3, res=0.1)

    zoning_area.commercial = sigmoid(1, -5, 1.5)
    zoning_area.residential = gauss(c=2, b=5, c_m=1)
    zoning_area.industrial = sigmoid(1, 5, 2.5)

    return zoning_area
