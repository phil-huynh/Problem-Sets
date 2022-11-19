def pizza_satisfaction(pizza_size, cheese_multiplier):
    if pizza_size >= 12 and cheese_multiplier == 3:
        return "maximally satisfied"
    elif pizza_size >= 10 and cheese_multiplier >= 2:
        return "really satisfied"
    else:
        return "very satisfied"