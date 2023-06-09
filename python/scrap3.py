

students = [
    "Stan",
    "Kyle",
    "Cartman",
    "Kenny",
    "Butters",
    "Craig",
    "Clyde",
    "Tweek",
    "Tolken",
    "Wendy",
    "Bebe",
    "Jimmy",
    "Timmy"
]

sent_attendance_token = [
    "Stan",
    "Kyle",
    "Butters",
    "Craig",
    "Tweek",
    "Tolken",
    "Wendy",
    "Bebe",
    "Jimmy",
    "Timmy"
]

did_exploration = [
    "Butters",
    "Craig",
    "Kyle",
    "Tweek",
    "Tolken",
    "Wendy",
    "Bebe",
    "Jimmy",
    "Timmy"
]

finished_project = [
    "Stan",
    "Cartman",
    "Butters",
    "Craig",
    "Tweek",
    "Tolken",
    "Wendy",
    "Jimmy"
]

failed_assessment = ["Cartman", "Kenny", "Clyde", "Butters"]

def who_is_absent(students, sent_tokens):
    cache = {}
    absent = []
    for student in students:
        cache[student] = True
    for token in sent_tokens:
        cache[token] = False
    for kid in cache:
        if cache.get(kid):
            absent.append(kid)
    return absent

print(who_is_absent(students, sent_attendance_token))

# OUTPUT ==>  ['Cartman', 'Kenny', 'Clyde']


def who_skipped_the_exploration(students, exploration):
    cache = {}
    did_not_do_exploration = []
    for name in exploration:
        cache[name] = True
    for student in students:
        if not cache.get(student):
            did_not_do_exploration.append(student)
    return did_not_do_exploration

print(who_skipped_the_exploration(students, did_exploration))

# OUTPUT ==>  ['Stan', 'Cartman', 'Kenny', 'Clyde']


def who_finished_project_and_passed_assessment(projects, assessments):
    cache = {}
    passed_both = []
    for project in projects:
        cache[project] = True
    for assessment in assessments:
        cache[assessment] = False
    for student in cache:
        if cache.get(student):
            passed_both.append(student)
    return passed_both

print(who_finished_project_and_passed_assessment(finished_project, failed_assessment))

# OUTPUT ==>  ['Stan', 'Craig', 'Tweek', 'Tolken', 'Wendy', 'Jimmy']




# # Be aware of how .get() behaves with falsy values when you are using it in if statements

# example = {
#     "a":0,
#     "b":4,
#     "c":"x",
#     "d":"",
#     "e":True,
#     "f":False,
#     "g":[1, 2, 3],
#     "h":[],
#     "i":{"a_key": "a value"},
#     "j": {},
#     "k": None
# }

# keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]

# def something_to_know_about_the_get_method(dict):
#     result = []
#     for key in keys:
#         if dict.get(key):
#             result.append(key)
#     return result

# print(something_to_know_about_the_get_method(example))

# # OUTPUT ==> ['b', 'c', 'e', 'g', 'i']


# def using_variable_in_dictionary(dict):
#     result = []
#     for key in keys:
#         if key in dict:
#             result.append(key)
#     return result

# print(using_variable_in_dictionary(example))

# OUTPUT ==> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']



# company = [
#     {"name": "leah",
#      "position": "manager",
#      "rate": 55,
#      "hours": 15
#     },
#     {"name": "freddy",
#      "position": "manager",
#      "rate": 25,
#      "hours": 0
#     },
#     {"name": "isaac",
#      "rate": 20,
#      "hours": 20
#     },
#     {"name": "murphey",
#      "position": "worker",
#      "rate": 41,
#      "hours": 25
#     },
#     {"name": "phil",
#      "position": "worker",
#      "rate": 9,
#      "hours": 35
#     },
# ]


# def get_list_of_managers(company):
#     manager_list = []
#     for person in company:
#         if person.get("position") == "manager":
#             manager_list.append(person["name"])
#     return manager_list


# def get_list_of_workers(company):
#     worker_list = []
#     for person in company:
#         if person.get("position") == "worker":
#             worker_list.append(person["name"])
#     return worker_list


# def longest_name(company):
#     long_name = ""
#     for employee in company:
#         if len(employee["name"]) > len(long_name):
#             long_name = employee["name"]
#     return long_name


# def get_manager_pay(company):
#     total = 0
#     for person in company:
#         if person.get("position") == "manager":
#             total += person["rate"] * person["hours"]
#     return total

# def who_made_the_most(company):
#     made_most = ""
#     most_money = 0
#     for employee in company:
#         money = employee["rate"] * employee["hours"]
#         if money > most_money:
#             made_most = employee["name"]
#             most_money = money
#     return made_most



# sentence = "here is a sentence and there are letters in it and stuff this sentence is a long and crazy run on and we are going to count all occurences of each of the letters in this ridiculous sentence"

# def letter_occurences(strng):
#     result = ""
#     cache = {}
#     for letter in sentence:
#         if letter != " ":
#             if letter not in cache:
#                 cache[letter] = 0
#             cache[letter] += 1
#     for key in cache:
#         result += f"There are {cache[key]} {key}'s. "
#     return result






# nums = [2,4,6,8,10,12,3,5,6,6,7,8,9,7,5,5,89,8,6,78,9,87,5]

# def remove_duplicates(lst):
#     cache = {}
#     result = []
#     for item in lst:
#         if item not in cache:
#             cache[item] = True
#             result.append(item)
#     return result

# print(remove_duplicates(nums))



# print(remove_duplicates(nums))



# for [[letter, num times it occured],[...],[...],[...]]


# def all_are_even(nums):
#     for num in nums:
#         if num % 2 != 0:
#             return False
#     return True

# print("result", all_are_even(nums))


# storage = []
# for key in keys:
#     print("\n")
#     print("THIS IS WHAT IS IN THE DICTIONARY", my_dict[key])
#     if key in my_dict:
#         print("IN THE IF STATEMENT")
#         storage.append(key)
#     print("THIS IS STORAGE", storage)
# print(storage)



# from pprint import pprint





# nums = [2, 3, 4, 6, 8, 9, 10, 11, 12, 14, 16, 17]

# def get_even_numbers(numbers):
#     new_list =[]
#     for num in numbers:
#         print("\n")
#         if num % 2 != 0:
#             new_list.append(num)
#     return new_list

# print(get_even_numbers(nums))


# numbers = [34,6,6,8,365,645,73,568,356,8846,8,34,1,]




# nums = [2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 14, 16, 17]

# def get_even_numbers(numbers):
#     new_list =[]
#     for num in numbers:
#         if num % 2 == 0:
#             new_list.append(num)
#     return new_list

# print(get_even_numbers(nums))



