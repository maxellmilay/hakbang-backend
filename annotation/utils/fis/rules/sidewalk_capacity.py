from annotation.utils.fis.fuzzy_logic import fuzzy_AND, fuzzy_OR

def low_sidewalk_capacity(w, z, walkway_width, zoning_area):
    return fuzzy_OR(
        # Rule 1: Narrow walkway, commercial area
        fuzzy_AND(walkway_width.narrow(w), zoning_area.commercial(z))
    )

def moderate_sidewalk_capacity(w, z, walkway_width, zoning_area):
    return fuzzy_OR(
        # Rule 1: Midsize walkway, commercial area
        fuzzy_AND(walkway_width.midsize(w), zoning_area.commercial(z)),

        # Rule 2: Narrow walkway, industrial area
        fuzzy_AND(walkway_width.narrow(w), zoning_area.industrial(z)),

        # Rule 3: Midsize walkway, industrial area
        fuzzy_AND(walkway_width.midsize(w), zoning_area.industrial(z)),

        # Rule 4: Narrow walkway, residential area
        fuzzy_AND(walkway_width.narrow(w), zoning_area.residential(z))
    )

def high_sidewalk_capacity(w, z, walkway_width, zoning_area):
    return fuzzy_OR(
        # Rule 1: Wide walkway, commercial area
        fuzzy_AND(walkway_width.wide(w), zoning_area.commercial(z)),

        # Rule 2: Wide walkway, industrial area
        fuzzy_AND(walkway_width.wide(w), zoning_area.industrial(z)),

        # Rule 3: Midsize walkway, residential area
        fuzzy_AND(walkway_width.midsize(w), zoning_area.residential(z)),

        # Rule 4: Wide walkway, residential area
        fuzzy_AND(walkway_width.wide(w), zoning_area.residential(z))
    )
