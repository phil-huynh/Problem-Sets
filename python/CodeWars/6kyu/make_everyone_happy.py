# https://www.codewars.com/kata/61eeb6e7577f050037b17a2d/train/python

# Overview
# We often use smiley faces in correspondence with other people. They allow us to quickly show our reaction to the person(s) we are talking to.

# But one day you wanted to make your correspondence more joyful. So today you have the opportunity to make it happen.

# Task:
# In this kata, your task will be to replace sad emoticons with funny ones.

# The emoticons, will be represented from:

# Eyes: marked as :, ; or =
# Nose (optional): marked as - or ~
# Mouth: marked as ( or [
# Examples:
# smile("Howdy :(")  // should return "Howdy :)"
# smile("Never be sad =[")  // should return "Never be sad =]"
# smile("Change this `=(` and this `:[`")  // should return "Change this `=)` and this `:]`"

def smile(text):
    text = [x for x in text]
    eyes = [":", ";", "="]
    noses = ["-", "~"]
    smiles = { "[": "]", "(": ")"}
    result = ""
    for i in range(len(text)):
        if text[i] in eyes:
            try:
                if text[i + 1] in smiles:
                    text[i + 1] = smiles[text[i + 1]]
                if text[i + 1] in noses and text[i + 2] in smiles:
                    text[i + 2] = smiles[text[i + 2]]
                result += text[i]
            except IndexError:
                result += text[i]
        else:
            result += text[i]
    return result