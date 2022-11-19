def num_laundry_days(num_shirts, num_days, event_days):
    laundry_days = 0
    clean_shirts = num_shirts
    for day in range(num_days):
        if day in event_days:
            num_shirts += 1
            clean_shirts += 1
        if clean_shirts == 0:
            laundry_days += 1
            clean_shirts = num_shirts
        clean_shirts -= 1
    return laundry_days