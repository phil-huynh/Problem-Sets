from pprint import pprint


print("\n")
print("Here are the solutions to Scott's problem set")
print("------------------------------------------------------------------")

# <!-- DOUBLE INDEX:
# Create a fxn named “double_index” with two parameters: a list and an index number. The fxn should double the value of the list element at the specified index and return the list with the doubled value.
# If the index is not a valid index, the fxn should return the original list.

# Input: ([3,8,-10,12], 2) => Output: [3,8,-20,12]
# Input: ([3,8,-10,12], 6) => Output: [3,8,-10,12]

def double_index(list, index):
    if index >= 0 and index < len(list):
        list[index] *= 2
    return list


print("Double Index Output ==> ", double_index([3,8,-10,12], 2))



# REMOVE MIDDLE:
# Create a fxn named “remove_middle” which has three parameters: a list, a start number, an end number. The fxn should return a sub-list of the list containing all of the elements between the start and end indexes.

# Input: ([4,8,15,16,23,42], 1, 3]) => Output: [8,15,16]

def remove_middle(list, start, end):
    return list[start:end + 1]


print("\n")
print("Remove Middle Output ==>", remove_middle([4,8,15,16,23,42], 1, 3))



# MORE THAN N
# Create a fxn named “more_than_n” that has three parameters: a list, an item, and a number. The fxn should return “True” if the item appears more then the number of times specified. Otherwise, the fxn should return “False”.

# Input: ([2,4,6,2,3,2,1,2], 2, 3) => Output: True
# Input: ([2,4,6,2,3,2,1,2], 4, 3) => Output: False

def more_than_n(list, item, number):
    count = 0
    for num in list:
        if num == item:
            count += 1
        if count > number:
            return True
    return False


print("\n")
print("More than n Output ==> ",more_than_n([2,4,6,2,3,2,1,2], 2, 3))
print("More than n Output ==> ",more_than_n([2,4,6,2,3,2,1,2], 4, 3))



# MORE FREQUENT ITEM
# Create a fxn named “most_frequent_item” that has three parameters: a list, a first item, a second item. Return either the first item or the second item depending on which occurs more often in the list. If the two items appear the same number of times, return the first item.

# Input: ([2,3,3,2,3,2,3,2,3], 2, 3) => Output: 3
# Input: ([2,3,3,2,3,2,3,2], 2, 3) => Output: 2

def more_frequent_item(list, item1, item2):
    total1 = 0
    total2 = 0
    for num in list:
        if num == item1:
            total1 += 1
        if num == item2:
            total2 += 1
    if total2 > total1:
        return item2
    return item1


print("\n")
print("More frequent item Output ==>", more_frequent_item([2,3,3,2,3,2,3,2,3], 2, 3))
print("More frequent item Output ==>", more_frequent_item([2,3,3,2,3,2,3,2], 2, 3))


# MIDDLE ITEM
# Create a fxn named “middle_element” that has one parameter: a list. If there are an odd number of elements in the list, return the middle element. If there are an even number, return the average of the middle elements.

# Input: ([5,2,-10,-4,4,5]) => Output: -7
# Input: ([5,2,-10,-4,4,]) => Output: -10

def middle_item(list):
    i = len(list)//2
    if len(list) % 2 == 0:
        return (list[i] + list[i-1])//2
    return list[i]


print("\n")
print("Middle Item ==>", middle_item([5,2,-10,-4,4,5]))
print("Middle Item ==>", middle_item([5,2,-10,-4,4,]))


# APPEND SUM
# Create a fxn named “append_sum” that has one parameter: a list. The fxn should add the last two elements of the list together and add the result to the end of the list. It should perform this process three times and then return the list.

# Input: ([1,1,2]) => Output: [1,1,2,3,5,8]


def append_sum(list):
    count = 3
    while count:
        list.append(list[-2] + list[-1])
        count -= 1
    return list


print("\n")
print("Append sum Output ==> ", append_sum([1,1,2]))



# COMBINE SORT
# Create a fxn named “combine_sort” that has two parameters: two lists. The fxn should combine the two lists into a new list, sort the result, and then return the new list.

# Input: ([4,10,2,5], [-10,2,5,10]) => Output: [-10,2,2,4,5,5,10,10]

def combine_sort(list1, list2):
    new_list = list1 + list2
    new_list.sort()
    return new_list


print("Combine sort Output ==> ", combine_sort([4,10,2,5], [-10,2,5,10]))



# APPEND SIZE
# Create a fxn named “append_size” that has one parameter: a list. The fxn should add all of the numbers between 1 and the size of the list to the end of the list, and then return the list.

# Input: ([23,42,108]) => Output: [23,42,108,1,2,3]

def append_size(list):
    for i in range(1, len(list) + 1):
        list.append(i)
    return list


print("\n")
print("Append size Output ==> ", append_size([23,42,108]))



# EVERY THREE NUMS
# Create a fxn named “every_three_nums” that has one parameter: a number. The fxn should return a list of every third number between the number passed in and 100 (inclusive). If the number passed in is greater then 100, it should return and empty list.

# Input: (91) => Output: [91, 94,97,100]
# Input: (106) => Output: []

def every_three_nums(number):
    result = []
    for num in range(number, 101, 3):
        result.append(number)
    return result


print("\n")
print("Every 3 Numbers Output ==> ", every_three_nums(91))
print("Every 3 Numbers Output ==> ", every_three_nums(106))



# GREETINGS
# Create a fxn named “greetings” that has one parameter: a list of names. In the fxn add the string “Hello” in front of each name and return the list.

# Input: ([“Sam”, “Jim”, “Sophie”]) => Output: [“Hello, Sam”, “Hello, Jim”, “Hello, Sophie”]

def greetings(names):
    result = []
    for name in names:
        result.append(f"Hello {name}")
    return result


print("\n")
print("Greetings Output ==> ", greetings(["Sam", "Jim", "Sophie"]))



# MAX NUM
# Create a fxn called “max_num” that has one parameter: a list of numbers. The fxn should return the largest number in the list

# Input: ([-10,0,20,50,75,15]) => Output: 75

def max_num(list):
    largest = 0
    for number in list:
        if number > largest:
            largest = number
    return largest


print("\n")
print("Max Num Output ==> ", max_num([-10,0,20,50,75,15]))



# SAME VALUES
# Create a fxn “same_values” that has two parameters: 2 lists of equal size. The fxn should return a list of indexes where there are equal values in each list.

# Input: ([5,1,-10,3,3], [5,10,-10,3,5]) => Output: [0,2,3]

# Bonus: try to solve this if you have 2 lists of unequal size

def same_values(list1, list2):
    index = 0
    result = []
    while list1 and list2:
        if list1[0] == list2[0]:
            result.append(index)
        index += 1
        list1 = list1[1:]
        list2 = list2[1:]
    return result


print("\n")
print("Same values Output ==> ", same_values([5,1,-10,3,3], [5,10,-10,3,5]))
print("Same values Output ==> ", same_values([5,1,-10,3,3,6,2,8], [5,10,-10,3,5,6]))



# REVERSED LIST
# Create a fxn named “reversed_list” that has 2 parameters: 2 lists. If the first list is the same as the second list reversed, the fxn should return “True”. If not, it should return “False”.

# Input: ([1,2,3],[3,2,1]) => Output: True
# Input: ([1,5,3],[3,2,1]) => Output: False

def reversed_list(list1, list2):
    for i in range(len(list1)):
        if list1[i] != list2[-(i + 1)]:
            return False
    return True



print("\n")
print("Reversed list Output ==> ", reversed_list([1,2,3],[3,2,1]))
print("Reversed list Output ==> ", reversed_list([1,5,3],[3,2,1]))


# MAKE SPOONERISM
# Create a fxn named “make_spoonerism” that has 2 parameters: 2 strings. The fxn should return the two words with the first letters switched.

# Input: (“Hello”, “John”) => Output: Jello Hohn

def make_spoonerism(w1,w2):
    new_w1 = f"{w2[0]}{w1[1:]}"
    new_w2 = f"{w1[0]}{w2[1:]}"
    return f"{new_w1} {new_w2}"


print("\n")
print("Make Spoonerism Output ==> ", make_spoonerism("Hello", "John"))



# SUM VALUES
# Create a fxn named “sum_values” that takes one parameter: a dictionary. The fxn should return the sum of the values in the dictionary.

# Input: ({"milk": 5, "eggs": 2, "flour": 3}) => Output: 10

def sum_values(dictionary):
    total = 0
    for item in dictionary:
        total += dictionary[item]
    return total


print("\n")
print("Sum Vaules Output ==> ", sum_values({"milk": 5, "eggs": 2, "flour": 3}))



# EVEN KEYS
# Create a fxn named “sum_even_keys” that takes in one parameter: a dictionary. The fxn should return the sum of all of the even key"s values.

# Input: ({1: 5, 2: 2, 3: 3}) => Output: 2
# Input: ({100: 5, 1000: 2, 10: 3}) => Output: 10

def even_keys(dictionary):
    total = 0
    for key in dictionary:
        if key % 2 == 0:
            total += dictionary[key]
    return total


print("\n")
print("Even keys Output ==> ", even_keys({1: 5, 2: 2, 3: 3}))
print("Even keys Output ==> ", even_keys({100: 5, 1000: 2, 10: 3}))


# ADD TEN
# Create a fxn named “add_ten” that takes in one parameter: a dictionary. The fxn should add 10 to every value in the dictionary and then return it.

# Input: ({1: 5, 2: 2, 3: 3}) => Output: {1: 15, 2: 12, 3: 13}

def add_ten(dictionary):
    for key in dictionary:
        dictionary[key] += 10
    return dictionary


print("\n")
print("Add ten Output ==> ", add_ten({1: 5, 2: 2, 3: 3}))



# VALUES THAT ARE KEYS
# Create a fxn named “values_are_keys” that takes in one parameter: a dictionary. The fxn should return a list of values that also equal keys.

# Input: ({1: 100, 2: 1, 3: 4, 4: 10}) => Output: [1, 4]
# Input: ({"a": "apple", "b": "a", "c": 100}) => Output: ["a"]

def values_that_are_keys(dictionary):
    keys = []
    for key in dictionary:
        if dictionary[key] in dictionary:
            keys.append(dictionary[key])
    return keys


print("\n")
print("Values that are keys Output ==> ", values_that_are_keys({1: 100, 2: 1, 3: 4, 4: 10}))
print("Values that are keys Output ==> ", values_that_are_keys({"a": "apple", "b": "a", "c": 100}))



# LARGEST VALUE
# Create a fxn named “max_key” that takes in one parameter: a dictionary. The fxn should return the key associated with the largest value.

# Input: ({1: 100, 2: 1, 3: 4, 4: 10}) => Output: 1
# Input: ({"a": 100, "b": 10, "c": 1000}) => Output: c


def largest_value(dictionary):
    largest = 0
    key_of_largest = None
    for key in dictionary:
        if dictionary[key] > largest:
            largest = dictionary[key]
            key_of_largest = key
    return key_of_largest

print("\n")
print("Largest Value Output ==> ", largest_value({1: 100, 2: 1, 3: 4, 4: 10}))
print("Largest Value Output ==> ", largest_value({"a": 100, "b": 10, "c": 1000}))

# WORD LENGTH DICTIONARY
# Create a fxn named ”word_length_dict” that takes in one parameter: a list of strings. The fxn should return a dictionary where each key is a word in the word list and the value is the length of that word.

# Input: ([“apple”, “cat”, “pickle”]) => Output: {"apple": 5, "cat": 3, "pickle": 6} -->

def word_length_dictionary(words):
    cache = {}
    for word in words:
        cache[word] = len(word)
    return cache

print("\n")
print("Word length dictionary Output ==> ", word_length_dictionary(["apple", "cat", "pickle"]))
print("\n")



# FREQUENCY COUNT
# Create a fxn named “frequency_count” that takes in one parameter: a list. The fxn should return a dictionary containing the frequency of each element in the list.

# Input: (["apple", "apple", "cat", 1]) => Output: {"apple": 2, "cat": 1, 1:1}
# Input: ([0,0,0,0,0]) => Output: {0: 5}

def frequency_count(list):
    cache = {}
    for item in list:
        if item not in cache:
            cache[item] = 0
        cache[item] += 1
    return cache


print("\n")
print("Frequency count ==> ", frequency_count(["apple", "apple", "cat", 1]))
print("Frequency count ==> ", frequency_count([0,0,0,0,0]))



# UNIQUE VALUES
# Create a fxn named “unique_values” that takes in one parameter: a dictionary. The fxn should return the number of unique values in the dictionary.

# Input: ({0: 3, 1: 1, 4: 1, 5: 3}) => Output: 2
# Input: ({0: 3, 1: 3, 4: 3, 5: 3}) => Output: 1
# Input: ({0: 3, 1: 6, 4: 9, 5: 1}) => Output: 4

def unique_values(dictionary):
    cache = {}
    for key in dictionary:
        cache[dictionary[key]] = True
    return len(cache.keys())

print("\n")
print("Unique value Output ==> ", unique_values({0: 3, 1: 1, 4: 1, 5: 3}))
print("Unique value Output ==> ", unique_values({0: 3, 1: 3, 4: 3, 5: 3}))
print("Unique value Output ==> ", unique_values({0: 3, 1: 6, 4: 9, 5: 1}))


# COUNT FIRST LETTER
# Create a fxn named “count_first_letter” that takes in one parameter: a dictionary with a last name as a key and a list of first names as the value. The fxn should return a dictionary where each key is the first letter of the last name and the value is the number of people whose last name begins with that letter.

# Input: ({"Stark": ["Ned", "Robb", "Sansa], "Snow": ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}) Output: {"S": 4, "L": 3}

def count_first_letter(dictionary):
    cache = {}
    for name in dictionary:
        if name[0] not in cache:
            cache[name[0]] = 0
        cache[name[0]] += len(dictionary[name])
    return cache


print("\n")
print("Count first letter Output ==> ", count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow": ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))


# GET CHANGE
# Create a fxn named “get_change” that gets user input for a cash total. Calculate the total number of Quarters / Dimes / Nickels / Pennies for the change exchange. The fxn should return a print of those calculations.
# Note: make this a “hungry” fxn that gets the largest number of large coins and smallest number of small coins.
# Note: validate the input to ensure proper input from the user, cover all edge case entries, do not allow breaking errors

# Input: 1.49
# Output:
# Total Cents: 149
# Total Quarters: 5
# Total Dimes: 2
# Total Nickels: 0
# Total Pennies: 4


def get_change(amount):
    amount *= 100
    result = [" ", f"Total Cents: {int(amount)}           "]
    denominations = [25, 10, 5]
    denom_names = ["Quarters", "Dimes", "Nickels"]
    for i, coin in enumerate(denominations):
        num_coins = amount//coin
        result.append(f"Total {denom_names[i]}: {int(num_coins)}           ")
        amount -= (num_coins * coin)
    if amount:
        result.append(f"Total Pennies: {int(amount)}                         ")
    return "\n".join(result)

print("\n")
print("Here is our count change printout")
print("-------------------------------------")
pprint(get_change(1.49))
print("\n\n\n")


