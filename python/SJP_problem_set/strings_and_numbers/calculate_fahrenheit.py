# **Calculate Fahrenheit**

# If you've spent time in the U.S., then you know that temperatures are communicated in the Fahrenheit scale, which can lead to some weird trans-Atlantic conversations:

# "How's the weather in Nairobi, Elinah?"

# "It's so hot! It's 32 outside!"

# "What? But that's freezing!"

# It'd be good to write a function that takes a value in Celsius and converts it to Fahrenheit for the non-metric folx of the U.S.

# This is the formula to convert Fahrenheit to Celsius:

# �=59×(�−32)

# You need to reverse that formula so you have a formula to calculate Celsius to Fahrenheit.

# 4**Calculate Fahrenheit**Submitted on 10/07/2022
# Given the value `celsius`, complete the function `calculate_fahrenheit` so that it returns the corresponding temperature in Fahrenheit.

# **Constraint**: `-40 <= celsius <= 40`

# Here are some example inputs and return values:`celsius`Return valueReason`032`0C is 32F`1050`10C is 50F
# It's guaranteed that `celsius` will be chosen so that the corresponding value in Fahrenheit will be an exact integer.

def calculate_fahrenheit(celsius):
    return celsius * (9/5) + 32