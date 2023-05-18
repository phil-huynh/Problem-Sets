# Strong agreements

# An interesting aspect of texting is adding more letters when you strongly agree with something.

# One such phenomenon is the word "Yas!" When someone strongly agrees with you, they could write, "Yaaaaaaas!"

# Given the integer `num_a`, complete the function `yas` so that it returns the word "Yas!" with that number of "a" letters in it.

# **Constraint**: `1 <= num_a <= 30`.

# Here are some example inputs and return values:`num_a`Return valueReason`1Yas!`The word has one "a"`5Yaaaaas!`The word has five "a"s`10Yaaaaaaaaaas!`The word has ten "a"s

def yas(num_a):
    return f"Y{num_a *'a'}s!"