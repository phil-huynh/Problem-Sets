def scammer(number):
    num = str(number)
    if ((num[0] == "2" or num[0] == "4")
        and (num[4] == "2" or num[4] == "4")
        and (num[6] == num[7])
        and (num[9] == "0")):
        return "ignore"
    else:
        return "accept"