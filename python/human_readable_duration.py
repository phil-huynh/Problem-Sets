def round_num(num):
    return int(str(num).split('.')[0])

def format_duration(seconds):
    if seconds == 0:
        return "now"

    cache = {
      "year": 0,
      "day": 0,
      "hour": 0,
      "minute": 0,
      "second": 0
    }

    if seconds/31536000 >= 1:
        cache["year"] = round_num(seconds/31536000)
        seconds = seconds % 31536000

    if seconds/86400 >= 1:
        cache["day"] = round_num(seconds/86400)
        seconds = seconds % 86400

    if seconds/3600 >= 1:
        cache["hour"] = round_num(seconds/3600)
        seconds = seconds % 3600

    if seconds/60 >= 1:
        cache["minute"] = round_num(seconds/60)
        seconds = seconds % 60
    cache["second"] = seconds
    units = []

    for key in cache:
        if cache[key] != 0:
            units.append(key)

    result = ""
    for i, unit in enumerate(units):
        if i == len(units) - 1:
            return f"{result}{cache[unit]} {unit}" if cache[unit] == 1 else f"{result}{cache[unit]} {unit}s"
        if i == len(units) - 2:
            if cache[unit] == 1:
                result = f"{result}{cache[unit]} {unit} and "
            else:
                result = f"{result}{cache[unit]} {unit}s and "
        else:
            if cache[unit] == 1:
                result = f"{result}{cache[unit]} {unit}, "
            else:
                result = f"{result}{cache[unit]} {unit}s, "
    return result