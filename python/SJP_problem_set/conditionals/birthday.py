def calories(entree_num, side_num, dessert_num, drink_num):
    entrees = {
      0: 0,
      1: 522,
      2: 399,
      3: 501
    }
    sides = {
      0: 0,
      1: 130,
      2: 125,
      3: 72
    }
    desserts = {
      0: 0,
      1: 222,
      2: 391,
      3: 100
    }
    drinks = {
      0: 0,
      1: 10,
      2: 8,
      3: 120
    }
    return entrees[entree_num] + sides[side_num] + desserts[dessert_num] + drinks[drink_num]