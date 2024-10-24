import numpy as np

def fuzzy_OR(*args):
    return np.max(args)

def fuzzy_AND(*args):
    return np.min(args)

def defuzzify(fuzzy_tup):
    return np.min([0*fuzzy_tup[0] + 50*fuzzy_tup[1] + 100*fuzzy_tup[2], 100])
