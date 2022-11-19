def sentiment(message):
    happy_check = message.split(":-)")
    sad_check = message.split(":-(")
    if len(happy_check) == 1 and len(sad_check) == 1:
        return "none"
    if len(happy_check) == len(sad_check):
        return "unsure"
    if len(happy_check) > len(sad_check):
        return "happy"
    if len(happy_check) < len(sad_check):
        return "sad"