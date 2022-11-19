def valid_password(password):
    if len(password) < 8 or len(password) > 12:
        return "bad"
    uppers = 0
    lowers = 0
    digits = 0

    for char in password:
        if char.isupper():
            uppers += 1
        if char.islower():
            lowers += 1
        if char.isdigit():
            digits += 1

    if lowers >= 2 and uppers >= 3 and digits >= 2:
        return "good"
    return "bad"