# **A far away galaxy**

# There has been a resurgence of new shows in the Star Wars saga, like *The Mandalorian* and *The Book of Boba Fett*. But, the movie that started it all, *Star Wars*, has an iconic opening scene where these words scroll up the screen:

# > A long time ago in a galaxy far, far away...
# >

# Have you ever wondered how far away that galaxy really is?

# In the above example, the word "far" is repeated twice. However, it'd be great if we could have some fun with it and have it return the sentence with as many "far"s as we want (within reason).

# Given the integer `num_fars`, complete the function `new_hope` so that it returns the sentence, "A long time ago in a galaxy far, far away" with `num_fars` occurrences of the word "far".
# There should be a comma right after each "far" **except for the last one**.

# **Constraint**: `1 <= num_os <= 6`.

# Here are some example inputs and return values:`num_fars`Return valueReason`1A long time ago in a galaxy far away...`Only one "far"`2A long time ago in a galaxy far, far away...`It has two "far"s with a comma after the first one`4A long time ago in a galaxy far, far, far, far away...`It has four "far"s with a comma after all but the last
# Make sure to return the **exact sentence**!

def new_hope(num_fars):
    beginning = "A long time ago in a galaxy"
    ending = " far away..."
    return f"{beginning}{(num_fars - 1) * ' far,'}{ending}"