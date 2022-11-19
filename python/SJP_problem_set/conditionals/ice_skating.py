def skating_day_message(month_num, day_num):
    if month_num == 12:
        if day_num == 4:
            return "YAY! It's World Ice Skating Day!"
        if day_num > 4:
            return "You just missed it. There's another next year!"
    if month_num < 12 or (month_num == 12 and day_num < 4):
        return "World Ice Skating Day is coming up!"
