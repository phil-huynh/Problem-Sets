# The eldest child

# You know a family with three children. The ages of the children form an *arithmetic sequence*. That means that the number of years between the ages of the youngest child and middle child is the same number of years between the ages of the middle child and the eldest child.

# For example, their ages could be 5, 10 and 15. The difference in age between the youngest child and middle child is 5 years. The difference in age between the middle child and the eldest child is 5 years.

# Given the ages of the youngest and middle children, what is the age of the eldest child?


# Given the integers `youngest_age` and `middle_age`, complete the function `calculate_eldest_age` so that it returns the age of the oldest sibling.

# **Constraints**:
# • `0 <= youngest_age <= 50`
# • `youngest_age <= middle_age <= 50`

# Here are some example inputs and return values:`youngest_agemiddle_age`Return valueReason`0510`The difference between the ages is 5 years`101112`The difference between the ages is 1 year`51729`The difference between the ages is 12 years


def calculate_eldest_age(youngest_age, middle_age):
    return middle_age + (middle_age - youngest_age)