from annotation.utils.fis.fuzzy_logic import fuzzy_AND, fuzzy_OR

def low_safety_risk(g, s, sf, bb, gradient, surface, street_furniture, lighting_score, border_buffer):
  return fuzzy_OR(
      # Rule 1: Accessible	Smooth	Does not obstruct	Exists	Good
      fuzzy_AND(gradient.accessible(g), surface.smooth(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting_score.good),

      # Rule 2: Accessible	Smooth	Does not obstruct	Does not Exist	Good
      fuzzy_AND(gradient.accessible(g), surface.smooth(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting_score.good),

      # Rule 3: Accessible	Cracked	Does not obstruct	Exists	Good
      fuzzy_AND(gradient.accessible(g), surface.cracked(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting_score.good),

      # Rule 4: Accessible	Cracked	Does not obstruct	Does not Exist	Good
      fuzzy_AND(gradient.accessible(g), surface.cracked(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting_score.good),

      # Rule 5: Inacessible	Smooth	Does not obstruct	Exists	Good
      fuzzy_AND(gradient.inaccessible(g), surface.smooth(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting_score.good),

      # Rule 6: Inacessible	Cracked	Does not obstruct	Exists	Good
      fuzzy_AND(gradient.inaccessible(g), surface.cracked(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting_score.good),
  )

def moderate_safety_risk(g, s, sf, bb, gradient, surface, street_furniture, lighting_score, border_buffer):
  return fuzzy_OR(
      # Rule 1: Accessible	Smooth	Obstructs	Exists	Good
      fuzzy_AND(gradient.accessible(g), surface.smooth(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting_score.good),

      # Rule 2: Accessible	Smooth	Obstructs	Exists	Moderate
      fuzzy_AND(gradient.accessible(g), surface.smooth(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting_score.moderate),

      # Rule 3: Accessible	Smooth	Obstructs	Does not Exist	Good
      fuzzy_AND(gradient.accessible(g), surface.smooth(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting_score.good),

      # Rule 4: Accessible	Smooth	Does not obstruct	Exists	Moderate
      fuzzy_AND(gradient.accessible(g), surface.smooth(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting_score.moderate),

      # Rule 5: Accessible	Smooth	Does not obstruct	Does not Exist	Moderate
      fuzzy_AND(gradient.accessible(g), surface.smooth(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting_score.moderate),

      # Rule 6: Accessible	Cracked	Obstructs	Exists	Good
      fuzzy_AND(gradient.accessible(g), surface.cracked(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting_score.good),

      # Rule 7: Accessible	Cracked	Does not obstruct	Exists	Moderate
      fuzzy_AND(gradient.accessible(g), surface.cracked(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting_score.moderate),

      # Rule 8: Accessible	Cracked	Does not obstruct	Does not Exist	Moderate
      fuzzy_AND(gradient.accessible(g), surface.cracked(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting_score.moderate),

      # Rule 9: Accessible	Damaged	Does not obstruct	Exists	Good
      fuzzy_AND(gradient.accessible(g), surface.damaged(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting_score.good),

      # Rule 10: Accessible	Damaged	Does not obstruct	Exists	Moderate
      fuzzy_AND(gradient.accessible(g), surface.damaged(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting_score.moderate),

      # Rule 11: Accessible	Damaged	Does not obstruct	Does not Exist	Good
      fuzzy_AND(gradient.accessible(g), surface.damaged(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting_score.good),

      # Rule 12: Inacessible	Smooth	Obstructs	Exists	Good
      fuzzy_AND(gradient.inaccessible(g), surface.smooth(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting_score.good),

      # Rule 13: Inacessible	Smooth	Does not obstruct	Exists	Moderate
      fuzzy_AND(gradient.inaccessible(g), surface.smooth(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting_score.moderate),

      # Rule 14: Inacessible	Smooth	Does not obstruct	Does not Exist	Good
      fuzzy_AND(gradient.inaccessible(g), surface.smooth(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting_score.good),

      # Rule 15: Inacessible	Cracked	Obstructs	Exists	Good
      fuzzy_AND(gradient.inaccessible(g), surface.cracked(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting_score.good),

      # Rule 16: Inacessible	Cracked	Does not obstruct	Exists	Moderate
      fuzzy_AND(gradient.inaccessible(g), surface.cracked(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting_score.moderate),

      # Rule 17: Inacessible	Cracked	Does not obstruct	Does not Exist	Good
      fuzzy_AND(gradient.inaccessible(g), surface.cracked(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting_score.good),

      # Rule 18: Inacessible	Damaged	Does not obstruct	Exists	Good
      fuzzy_AND(gradient.inaccessible(g), surface.damaged(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting_score.good),
  )

def high_safety_risk(g, s, sf, bb, gradient, surface, street_furniture, lighting_score, border_buffer):
  return fuzzy_OR(
      # Rule 1: Accessible	Smooth	Obstructs	Exists	Bad
      fuzzy_AND(gradient.accessible(g), surface.smooth(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting_score.bad),

      # Rule 2: Accessible	Smooth	Obstructs	Does not Exist	Moderate
      fuzzy_AND(gradient.accessible(g), surface.smooth(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting_score.moderate),

      # Rule 3: Accessible	Smooth	Obstructs	Does not Exist	Bad
      fuzzy_AND(gradient.accessible(g), surface.smooth(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting_score.bad),

      # Rule 4: Accessible	Smooth	Does not obstruct	Exists	Bad
      fuzzy_AND(gradient.accessible(g), surface.smooth(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting_score.bad),

      # Rule 5: Accessible	Smooth	Does not obstruct	Does not Exist	Bad
      fuzzy_AND(gradient.accessible(g), surface.smooth(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting_score.bad),

      # Rule 6: Accessible Cracked Obstructs Exists Moderate
      fuzzy_AND(gradient.accessible(g), surface.cracked(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting_score.moderate),

      # Rule 7: Accessible	Cracked	Obstructs	Exists	Bad
      fuzzy_AND(gradient.accessible(g), surface.cracked(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting_score.bad),

      # Rule 8: Accessible	Cracked	Obstructs	Does not Exist	Good
      fuzzy_AND(gradient.accessible(g), surface.cracked(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting_score.good),

      # Rule 9: Accessible	Cracked	Obstructs	Does not Exist	Moderate
      fuzzy_AND(gradient.accessible(g), surface.cracked(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting_score.moderate),

      # Rule 10: Accessible	Cracked	Obstructs	Does not Exist	Bad
      fuzzy_AND(gradient.accessible(g), surface.cracked(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting_score.bad),

      # Rule 11: Accessible	Cracked	Does not obstruct	Exists	Bad
      fuzzy_AND(gradient.accessible(g), surface.cracked(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting_score.bad),

      # Rule 12: Accessible	Cracked	Does not obstruct	Does not Exist	Bad
      fuzzy_AND(gradient.accessible(g), surface.cracked(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting_score.bad),

      # Rule 13: Accessible	Damaged	Obstructs	Exists	Good
      fuzzy_AND(gradient.accessible(g), surface.damaged(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting_score.good),

      # Rule 14: Accessible	Damaged	Obstructs	Exists	Moderate
      fuzzy_AND(gradient.accessible(g), surface.damaged(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting_score.moderate),

      # Rule 15: Accessible	Damaged	Obstructs	Exists	Bad
      fuzzy_AND(gradient.accessible(g), surface.damaged(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting_score.bad),

      # Rule 16: Accessible	Damaged	Obstructs	Does not Exist	Good
      fuzzy_AND(gradient.accessible(g), surface.damaged(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting_score.good),

      # Rule 17: Accessible	Damaged	Obstructs	Does not Exist	Moderate
      fuzzy_AND(gradient.accessible(g), surface.damaged(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting_score.moderate),

      # Rule 18: Accessible	Damaged	Obstructs	Does not Exist	Bad
      fuzzy_AND(gradient.accessible(g), surface.damaged(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting_score.bad),

      # Rule 19: Accessible	Damaged	Does not obstruct	Exists	Bad
      fuzzy_AND(gradient.accessible(g), surface.damaged(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting_score.bad),

      # Rule 20: Accessible	Damaged	Does not obstruct	Does not Exist	Moderate
      fuzzy_AND(gradient.accessible(g), surface.damaged(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting_score.moderate),

      # Rule 21: Accessible	Damaged	Does not obstruct	Does not Exist	Bad
      fuzzy_AND(gradient.accessible(g), surface.damaged(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting_score.bad),

      # Rule 22: Inacessible	Smooth	Obstructs	Exists	Moderate
      fuzzy_AND(gradient.inaccessible(g), surface.smooth(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting_score.moderate),

      # Rule 23: Inacessible	Smooth	Obstructs	Exists	Bad
      fuzzy_AND(gradient.inaccessible(g), surface.smooth(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting_score.bad),

      # Rule 24: Inacessible	Smooth	Obstructs	Does not Exist	Good
      fuzzy_AND(gradient.inaccessible(g), surface.smooth(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting_score.good),

      # Rule 25: Inacessible	Smooth	Obstructs	Does not Exist	Moderate
      fuzzy_AND(gradient.inaccessible(g), surface.smooth(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting_score.moderate),

      # Rule 26: Inacessible	Smooth	Obstructs	Does not Exist	Bad
      fuzzy_AND(gradient.inaccessible(g), surface.smooth(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting_score.bad),

      # Rule 27: Inacessible	Smooth	Does not obstruct	Exists	Bad
      fuzzy_AND(gradient.inaccessible(g), surface.smooth(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting_score.bad),

      # Rule 28: Inacessible	Smooth	Does not obstruct	Does not Exist	Moderate
      fuzzy_AND(gradient.inaccessible(g), surface.smooth(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting_score.moderate),

      # Rule 29: Inacessible	Smooth	Does not obstruct	Does not Exist	Bad
      fuzzy_AND(gradient.inaccessible(g), surface.smooth(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting_score.bad),

      # Rule 30: Inacessible	Cracked	Obstructs	Exists	Moderate
      fuzzy_AND(gradient.inaccessible(g), surface.cracked(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting_score.moderate),

      # Rule 31: Inacessible	Cracked	Obstructs	Exists	Bad
      fuzzy_AND(gradient.inaccessible(g), surface.cracked(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting_score.bad),

      # Rule 32: Inacessible	Cracked	Obstructs	Does not Exist	Good
      fuzzy_AND(gradient.inaccessible(g), surface.cracked(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting_score.good),

      # Rule 33: Inacessible	Cracked	Obstructs	Does not Exist	Moderate
      fuzzy_AND(gradient.inaccessible(g), surface.cracked(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting_score.moderate),

      # Rule 34: Inacessible	Cracked	Obstructs	Does not Exist	Bad
      fuzzy_AND(gradient.inaccessible(g), surface.cracked(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting_score.bad),

      # Rule 35: Inacessible	Cracked	Does not obstruct	Exists	Bad
      fuzzy_AND(gradient.inaccessible(g), surface.cracked(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting_score.bad),

      # Rule 36: Inacessible	Cracked	Does not obstruct	Does not Exist	Moderate
      fuzzy_AND(gradient.inaccessible(g), surface.cracked(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting_score.moderate),

      # Rule 37: Inacessible	Cracked	Does not obstruct	Does not Exist	Bad
      fuzzy_AND(gradient.inaccessible(g), surface.cracked(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting_score.bad),

      # Rule 38: Inacessible	Damaged	Obstructs	Exists	Good
      fuzzy_AND(gradient.inaccessible(g), surface.damaged(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting_score.good),

      # Rule 39: Inacessible	Damaged	Obstructs	Exists	Moderate
      fuzzy_AND(gradient.inaccessible(g), surface.damaged(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting_score.moderate),

      # Rule 40: Inacessible	Damaged	Obstructs	Exists	Bad
      fuzzy_AND(gradient.inaccessible(g), surface.damaged(s), street_furniture.obstructs(sf), border_buffer.exists(bb), lighting_score.bad),

      # Rule 41: Inacessible	Damaged	Obstructs	Does not Exist	Good
      fuzzy_AND(gradient.inaccessible(g), surface.damaged(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting_score.good),

      # Rule 42: Inacessible	Damaged	Obstructs	Does not Exist	Moderate
      fuzzy_AND(gradient.inaccessible(g), surface.damaged(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting_score.moderate),

      # Rule 43: Inacessible	Damaged	Obstructs	Does not Exist	Bad
      fuzzy_AND(gradient.inaccessible(g), surface.damaged(s), street_furniture.obstructs(sf), border_buffer.does_not_exist(bb), lighting_score.bad),

      # Rule 44: Inacessible	Damaged	Does not obstruct	Exists	Moderate
      fuzzy_AND(gradient.inaccessible(g), surface.damaged(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting_score.moderate),

      # Rule 45: Inacessible	Damaged	Does not obstruct	Exists	Bad
      fuzzy_AND(gradient.inaccessible(g), surface.damaged(s), street_furniture.does_not_obstruct(sf), border_buffer.exists(bb), lighting_score.bad),

      # Rule 46: Inacessible	Damaged	Does not obstruct	Does not Exist	Good
      fuzzy_AND(gradient.inaccessible(g), surface.damaged(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting_score.good),

      # Rule 47: Inacessible	Damaged	Does not obstruct	Does not Exist	Moderate
      fuzzy_AND(gradient.inaccessible(g), surface.damaged(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting_score.moderate),

      # Rule 48: Inacessible	Damaged	Does not obstruct	Does not Exist	Bad
      fuzzy_AND(gradient.inaccessible(g), surface.damaged(s), street_furniture.does_not_obstruct(sf), border_buffer.does_not_exist(bb), lighting_score.bad),
  )

