def read(r,b):
    red = True if r == "1" else False
    blue = True if b == "1" else False
    return red, blue

def button_sequences(seqR, seqB):
    colors = zip(seqR, seqB)
    red, blue= False, False
    result = ""
    for light in colors:
        last = result[-1] if result and not clear else None
        if not red and not blue:
            red, blue = read(light[0], light[1])
            if red:
                result += "R"
            if blue and not red:
                result += "B"
        elif red and blue:
            red, blue = read(light[0], light[1])
            if blue and not red and last != "B":
                result += "B"
            if red and not blue and last != "R":
                result += "R"
        elif red:
            red, blue = read(light[0], light[1])
            if blue and not red:
                result += "B"
            if red and last != "R":
                result += "R"
        elif blue:
            red, blue = read(light[0], light[1])
            if red and not blue:
                result += "R"
        clear = True if light[0] == "0" and light[1] == "0" else False
    return result

print(button_sequences("10011010", "10110111"))      #"RBRB"
print(button_sequences("01001000", "01011100"))      #"RB"
print(button_sequences("01101000", "00111000"))      #"RB"



