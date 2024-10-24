from annotation.utils.fis.fuzzy_logic import fuzzy_AND, fuzzy_OR

def low_safety_risk(g, s, sf, l, bb, gradient, surface, street_furniture, lighting, border_buffer):
    return fuzzy_OR(
        # Rule 1: Accessible, Smooth, Does not Obstruct, Exists, Adequate
        fuzzy_AND(gradient.accessible(g), surface.smooth(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting.adequate(l)),

        # Rule 2: Accessible, Smooth, Does not Obstruct, Exists, Excellent
        fuzzy_AND(gradient.accessible(g), surface.smooth(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting.excellent(l)),

        # Rule 3: Accessible, Cracked, Does not Obstruct, Exists, Adequate
        fuzzy_AND(gradient.accessible(g), surface.cracked(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting.adequate(l)),

        # Rule 4: Accessible, Cracked, Does not Obstruct, Exists, Excellent
        fuzzy_AND(gradient.accessible(g), surface.cracked(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting.excellent(l)),

        # Rule 5: Accessible, Smooth, Obstructs, Exists, Excellent
        fuzzy_AND(gradient.accessible(g), surface.smooth(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting.excellent(l)),

        # Rule 6: Inaccessible, Smooth, Does not Obstruct, Exists, Excellent
        fuzzy_AND(gradient.inaccessible(g), surface.smooth(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting.excellent(l))
    )

def moderate_safety_risk(g, s, sf, l, bb, gradient, surface, street_furniture, lighting, border_buffer):
    return fuzzy_OR(
        # Rule 1: Accessible, Smooth, Does not Obstruct, Does not Exist, Adequate
        fuzzy_AND(gradient.accessible(g), surface.smooth(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting.adequate(l)),

        # Rule 2: Accessible, Smooth, Obstructs, Exists, Poor
        fuzzy_AND(gradient.accessible(g), surface.smooth(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting.poor(l)),

        # Rule 3: Accessible, Smooth, Obstructs, Exists, Adequate
        fuzzy_AND(gradient.accessible(g), surface.smooth(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting.adequate(l)),

        # Rule 4: Accessible, Smooth, Obstructs, Does not Exist, Excellent
        fuzzy_AND(gradient.accessible(g), surface.smooth(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting.excellent(l)),

        # Rule 5: Accessible, Smooth, Does not Obstruct, Exists, Poor
        fuzzy_AND(gradient.accessible(g), surface.smooth(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting.poor(l)),

        # Rule 6: Accessible, Smooth, Does not Obstruct, Does not Exist, Excellent
        fuzzy_AND(gradient.accessible(g), surface.smooth(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting.excellent(l)),

        # Rule 7: Accessible, Cracked, Obstructs, Exists, Adequate
        fuzzy_AND(gradient.accessible(g), surface.cracked(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting.adequate(l)),

        # Rule 8: Accessible, Cracked, Obstructs, Exists, Excellent
        fuzzy_AND(gradient.accessible(g), surface.cracked(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting.excellent(l)),

        # Rule 9: Accessible, Cracked, Obstructs, Does not Exist, Excellent
        fuzzy_AND(gradient.accessible(g), surface.cracked(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting.excellent(l)),

        # Rule 10: Accessible, Cracked, Does not Obstruct, Exists, Poor
        fuzzy_AND(gradient.accessible(g), surface.cracked(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting.poor(l)),

        # Rule 11: Accessible, Cracked, Does not Obstruct, Does not Exist, Adequate
        fuzzy_AND(gradient.accessible(g), surface.cracked(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting.adequate(l)),

        # Rule 12: Accessible, Cracked, Does not Obstruct, Does not Exist, Excellent
        fuzzy_AND(gradient.accessible(g), surface.cracked(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting.excellent(l)),

        # Rule 13: Accessible, Damaged, Does not Obstruct, Exists, Adequate
        fuzzy_AND(gradient.accessible(g), surface.damaged(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting.adequate(l)),

        # Rule 14: Accessible, Damaged, Does not Obstruct, Exists, Excellent
        fuzzy_AND(gradient.accessible(g), surface.damaged(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting.excellent(l)),

        # Rule 15: Inaccessible, Smooth, Obstructs, Exists, Adequate
        fuzzy_AND(gradient.inaccessible(g), surface.smooth(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting.adequate(l)),

        # Rule 16: Inaccessible, Smooth, Obstructs, Exists, Excellent
        fuzzy_AND(gradient.inaccessible(g), surface.smooth(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting.excellent(l)),

        # Rule 17: Inaccessible, Smooth, Obstructs, Does not Exist, Excellent
        fuzzy_AND(gradient.inaccessible(g), surface.smooth(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting.excellent(l)),

        # Rule 18: Inaccessible, Smooth, Does not Obstruct, Exists, Adequate
        fuzzy_AND(gradient.inaccessible(g), surface.smooth(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting.adequate(l)),

        # Rule 19: Inaccessible, Smooth, Does not Obstruct, Does not Exist, Excellent
        fuzzy_AND(gradient.inaccessible(g), surface.smooth(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting.excellent(l)),

        # Rule 20: Inaccessible, Cracked, Obstructs, Exists, Adequate
        fuzzy_AND(gradient.inaccessible(g), surface.cracked(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting.adequate(l)),

        # Rule 21: Inaccessible, Cracked, Obstructs, Exists, Excellent
        fuzzy_AND(gradient.inaccessible(g), surface.cracked(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting.excellent(l)),

        # Rule 22: Inaccessible, Cracked, Obstructs, Does not Exist, Excellent
        fuzzy_AND(gradient.inaccessible(g), surface.cracked(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting.excellent(l)),

        # Rule 23: Inaccessible, Cracked, Does not Obstruct, Exists, Adequate
        fuzzy_AND(gradient.inaccessible(g), surface.cracked(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting.adequate(l)),

        # Rule 24: Inaccessible, Cracked, Does not Obstruct, Exists, Excellent
        fuzzy_AND(gradient.inaccessible(g), surface.cracked(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting.excellent(l)),

        # Rule 25: Inaccessible, Cracked, Does not Obstruct, Does not Exist, Excellent
        fuzzy_AND(gradient.inaccessible(g), surface.cracked(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting.excellent(l))
    )

def high_safety_risk(g, s, sf, l, bb, gradient, surface, street_furniture, lighting, border_buffer):
    return fuzzy_OR(
        # Rule 1: Accessible, Smooth, Obstructs, Does not Exist, Poor
        fuzzy_AND(gradient.accessible(g), surface.smooth(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting.poor(l)),

        # Rule 2: Accessible, Smooth, Obstructs, Does not Exist, Adequate
        fuzzy_AND(gradient.accessible(g), surface.smooth(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting.adequate(l)),

        # Rule 3: Accessible, Smooth, Does not Obstruct, Does not Exist, Poor
        fuzzy_AND(gradient.accessible(g), surface.smooth(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting.poor(l)),

        # Rule 4: Accessible, Cracked, Obstructs, Exists, Poor
        fuzzy_AND(gradient.accessible(g), surface.cracked(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting.poor(l)),

        # Rule 5: Accessible, Cracked, Obstructs, Does not Exist, Poor
        fuzzy_AND(gradient.accessible(g), surface.cracked(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting.poor(l)),

        # Rule 6: Accessible, Cracked, Obstructs, Does not Exist, Adequate
        fuzzy_AND(gradient.accessible(g), surface.cracked(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting.adequate(l)),

        # Rule 7: Accessible, Cracked, Does not Obstruct, Does not Exist, Poor
        fuzzy_AND(gradient.accessible(g), surface.cracked(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting.poor(l)),

        # Rule 8: Accessible, Damaged, Obstructs, Exists, Poor
        fuzzy_AND(gradient.accessible(g), surface.damaged(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting.poor(l)),

        # Rule 9: Accessible, Damaged, Obstructs, Exists, Adequate
        fuzzy_AND(gradient.accessible(g), surface.damaged(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting.adequate(l)),

        # Rule 10: Accessible, Damaged, Obstructs, Exists, Excellent
        fuzzy_AND(gradient.accessible(g), surface.damaged(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting.excellent(l)),

        # Rule 11: Accessible, Damaged, Obstructs, Does not Exist, Poor
        fuzzy_AND(gradient.accessible(g), surface.damaged(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting.poor(l)),

        # Rule 12: Accessible, Damaged, Obstructs, Does not Exist, Adequate
        fuzzy_AND(gradient.accessible(g), surface.damaged(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting.adequate(l)),

        # Rule 13: Accessible, Damaged, Obstructs, Does not Exist, Excellent
        fuzzy_AND(gradient.accessible(g), surface.damaged(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting.excellent(l)),

        # Rule 14: Accessible, Damaged, Does not Obstruct, Exists, Poor
        fuzzy_AND(gradient.accessible(g), surface.damaged(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting.poor(l)),

        # Rule 15: Accessible, Damaged, Does not Obstruct, Does not Exist, Poor
        fuzzy_AND(gradient.accessible(g), surface.damaged(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting.poor(l)),

        # Rule 16: Accessible, Damaged, Does not Obstruct, Does not Exist, Adequate
        fuzzy_AND(gradient.accessible(g), surface.damaged(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting.adequate(l)),

        # Rule 17: Accessible, Damaged, Does not Obstruct, Does not Exist, Excellent
        fuzzy_AND(gradient.accessible(g), surface.damaged(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting.excellent(l)),

        # Rule 18: Inaccessible, Smooth, Obstructs, Exists, Poor
        fuzzy_AND(gradient.inaccessible(g), surface.smooth(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting.poor(l)),

        # Rule 19: Inaccessible, Smooth, Obstructs, Does not Exist, Poor
        fuzzy_AND(gradient.inaccessible(g), surface.smooth(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting.poor(l)),

        # Rule 20: Inaccessible, Smooth, Obstructs, Does not Exist, Adequate
        fuzzy_AND(gradient.inaccessible(g), surface.smooth(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting.adequate(l)),

        # Rule 21: Inaccessible, Smooth, Does not Obstruct, Exists, Poor
        fuzzy_AND(gradient.inaccessible(g), surface.smooth(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting.poor(l)),

        # Rule 22: Inaccessible, Smooth, Does not Obstruct, Does not Exist, Poor
        fuzzy_AND(gradient.inaccessible(g), surface.smooth(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting.poor(l)),

        # Rule 23: Inaccessible, Smooth, Does not Obstruct, Does not Exist, Adequate
        fuzzy_AND(gradient.inaccessible(g), surface.smooth(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting.adequate(l)),

        # Rule 24: Inaccessible, Cracked, Obstructs, Exists, Poor
        fuzzy_AND(gradient.inaccessible(g), surface.cracked(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting.poor(l)),

        # Rule 25: Inaccessible, Cracked, Obstructs, Does not Exist, Poor
        fuzzy_AND(gradient.inaccessible(g), surface.cracked(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting.poor(l)),

        # Rule 26: Inaccessible, Cracked, Obstructs, Does not Exist, Adequate
        fuzzy_AND(gradient.inaccessible(g), surface.cracked(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting.adequate(l)),

        # Rule 27: Inaccessible, Cracked, Does not Obstruct, Exists, Poor
        fuzzy_AND(gradient.inaccessible(g), surface.cracked(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting.poor(l)),

        # Rule 28: Inaccessible, Cracked, Does not Obstruct, Does not Exist, Poor
        fuzzy_AND(gradient.inaccessible(g), surface.cracked(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting.poor(l)),

        # Rule 29: Inaccessible, Cracked, Does not Obstruct, Does not Exist, Adequate
        fuzzy_AND(gradient.inaccessible(g), surface.cracked(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting.adequate(l)),

        # Rule 30: Inaccessible, Damaged, Obstructs, Exists, Poor
        fuzzy_AND(gradient.inaccessible(g), surface.damaged(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting.poor(l)),

        # Rule 31: Inaccessible, Damaged, Obstructs, Exists, Adequate
        fuzzy_AND(gradient.inaccessible(g), surface.damaged(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting.adequate(l)),

        # Rule 32: Inaccessible, Damaged, Obstructs, Exists, Excellent
        fuzzy_AND(gradient.inaccessible(g), surface.damaged(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting.excellent(l)),

        # Rule 33: Inaccessible, Damaged, Obstructs, Does not Exist, Poor
        fuzzy_AND(gradient.inaccessible(g), surface.damaged(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting.poor(l)),

        # Rule 34: Inaccessible, Damaged, Obstructs, Does not Exist, Adequate
        fuzzy_AND(gradient.inaccessible(g), surface.damaged(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting.adequate(l)),

        # Rule 35: Inaccessible, Damaged, Obstructs, Does not Exist, Excellent
        fuzzy_AND(gradient.inaccessible(g), surface.damaged(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting.excellent(l)),

        # Rule 36: Inaccessible, Damaged, Does not Obstruct, Exists, Poor
        fuzzy_AND(gradient.inaccessible(g), surface.damaged(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting.poor(l)),

        # Rule 37: Inaccessible, Damaged, Does not Obstruct, Exists, Adequate
        fuzzy_AND(gradient.inaccessible(g), surface.damaged(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting.adequate(l)),

        # Rule 38: Inaccessible, Damaged, Does not Obstruct, Exists, Excellent
        fuzzy_AND(gradient.inaccessible(g), surface.damaged(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting.excellent(l)),

        # Rule 39: Inaccessible, Damaged, Does not Obstruct, Does not Exist, Poor
        fuzzy_AND(gradient.inaccessible(g), surface.damaged(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting.poor(l)),

        # Rule 40: Inaccessible, Damaged, Does not Obstruct, Does not Exist, Adequate
        fuzzy_AND(gradient.inaccessible(g), surface.damaged(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting.adequate(l)),

        # Rule 41: Inaccessible, Damaged, Does not Obstruct, Does not Exist, Excellent
        fuzzy_AND(gradient.inaccessible(g), surface.damaged(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting.excellent(l))
    )
