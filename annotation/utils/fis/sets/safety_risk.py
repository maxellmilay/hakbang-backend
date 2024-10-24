from fuzzylogic.classes import Domain
from fuzzylogic.functions import gauss, sigmoid

def gradient_membership():
    gradient = Domain("gradient", 0, 12, res=0.1)

    gradient.accessible = sigmoid(1, -3, 5)
    gradient.inaccessible = sigmoid(1, 3, 5)

    return gradient

def surface_membership():
    surface = Domain("surface", 0, 12, res=0.1)

    surface.smooth = sigmoid(1, -10, 5)
    surface.cracked = gauss(c=6, b=0.5, c_m=1)
    surface.damaged = sigmoid(1, 10, 6)

    return surface

def street_furniture_membership():
    street_furniture = Domain("street_furniture", 0, 3, res=0.1)

    street_furniture.obstructs = sigmoid(1, -9, 0.9)
    street_furniture.does_not_obstruct = sigmoid(1, 12, 1)

    return street_furniture

def border_buffer_membership():
    border_buffer = Domain("border_buffer", 0, 1, res=0.1)

    border_buffer.exists = sigmoid(1, -10, 0.5)
    border_buffer.does_not_exist = sigmoid(1, 10, 0.5)

    return border_buffer

def lighting_membership():
    lighting = Domain("lighting", 1, 3, res=0.1)

    lighting.poor = sigmoid(1, -7, 1.75)
    lighting.adequate = gauss(c=2, b=5, c_m=1)
    lighting.excellent = sigmoid(1, 7, 2.25)

    return lighting
