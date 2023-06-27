# from pprint import pprint

# unsortedQueue = [
#   { "taskId": 2, "isUrgent": True, "dueAt": 7, "patientId": "C", "providerId": "Z" },
#   { "taskId": 5, "isUrgent": False, "dueAt": 8, "patientId": "B", "providerId": "Z" },
#   { "taskId": 6, "isUrgent": False, "dueAt": 9, "patientId": "B", "providerId": "Y" },
#   { "taskId": 1, "isUrgent": True, "dueAt": 6, "patientId": "A", "providerId": "X" },
#   { "taskId": 7, "isUrgent": False, "dueAt": 5, "patientId": "C", "providerId": "X" },
#   { "taskId": 4, "isUrgent": False, "dueAt": 4, "patientId": "B", "providerId": "Y" },
#   { "taskId": 3, "isUrgent": False, "dueAt": 3, "patientId": "B", "providerId": "Z" }
# ]


# def next_due(queue):
#     due_first = queue[0]["patientId"]
#     time = queue[0]["dueAt"]
#     for patient in queue:
#         if patient["dueAt"] < time:
#             time = patient["dueAt"]
#             due_first = patient["patientId"]
#     return due_first


# def patient(group, patient):
#     current_patient = list(filter(lambda a: a["patientId"] == patient, group))
#     current_patient.sort(key=lambda a: a["dueAt"])
#     return current_patient


# def remove_patient(queue, patient):
#     return (list(filter(lambda a: a["patientId"] != patient, queue)))


# def schedule(queue):
#     final_list = []
#     while queue:
#         next_patient = next_due(queue)
#         final_list += patient(queue, next_patient)
#         queue = remove_patient(queue, next_patient)
#     return final_list


# def final_schedule(queue):
#     initial_schedule = schedule(queue)
#     urgent, not_urgent = [], []
#     for entry in initial_schedule:
#         urgent.append(entry) if entry["isUrgent"] else not_urgent.append(entry)
#     urgent.sort(key=lambda a: a["dueAt"])
#     return urgent + not_urgent



# arr1 = [1,2,3,4,5]
# arr2 = [9,8,7,6,5]
# arr3 = [11,12,13,14,15]

# arr1 = [*arr1, *[num*5 for num in arr2]]

# print(arr1)


# blu="\033[01;94m"
# g="\033[01;92m"
# y="\033[01;93m"
# p="\033[01;95m"
# r="\033[01;91m"
# cy="\033[01;96m"
# w="\033[01;97m"
# u="\033[04m"
# ru="\033[24m"
# cl="\033[00m"

# bblu="\033[44m"
# blbl="\033[104m"
# br="\033[41m"
# blr="\033[101m"
# bg="\033[42m"
# blg="\033[102m"
# by="\033[43m"
# bly="\033[103m"
# bp="\033[45m"
# blp="\033[105m"
# bc="\033[46m"
# blcy="\033[106m"

# bld="\033[01m"
# f="\033[02m"
# i="\033[03m"
# u="\033[04m"
# bl="\033[05m"
# rev="\033[07m"
# hid="\033[08m"

# rb="\033[21m"
# rf="\033[22m"
# ri="\033[23m"
# ru="\033[24m"
# rbl="\033[25m"
# rr="\033[27m"
# rh="\033[28m"

# blank_line = f"{hid}blank{rh}"
# sps = f"{hid} .{rh}"
# spe = f"{hid}. {rh}"
# sp3 = f"{hid} s {rh}"
# sp4 = f"{hid} sp {rh}"
# sp5 = f"{hid} spa {rh}"
# color_swap = False

# colors_and_effects = [blu,g,y,p,r,cy,w,cl,bblu,blbl,br,blr,bg,blg,by,bly,bp,blp,bc,blcy,bld,f,i,u,bl,rev,hid,rb,rf,ri,ru,rbl,rr,rh]
# special_characters = chars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "+", "=", "[", "]", "{", "}", "|", "\\", ";", "\"", "'", ",", ".", "/", "?", "<", ">", "`", "~", ":", " "]



# test1 = f"{spe}{g}cons1{p}: {g}prod1{p}@{cy}app{p},{g}prod2{p}@{cy}app {p}| {g}cons2{p}: {g}prod3{p}@{cy}app {p}| {g}cons3{y}...{cl}"
# test3 = f"  cons1: prod1@app,prod2@app | cons2: prod3@app | cons3..."

# print(test1)

# print(len(test3))


# def adjusted(string):
#     length = len(string)
#     adjust = 0
#     print(re.findall("\033\[[0-9;]+m", string))
#     for code in re.findall("\033\[[0-9;]+m", string):
#         adjust += len(code)
#     return length - adjust
# print("adjusted length ", adjusted(test1))
# print(len(spe))

import re


test = "test/8000/y/something: one, two, three"


formats = [
    "([\w]+\/[\d]+\/[a-z]\/[\w]+:[\w\s,]*)",
    "([\w]+\/[\d]+\/[a-z]\/[\w]+:)",
    "([\w]+\/[\d]+\/[a-z]\/:[\w\s,]*)",
    "([\w]+\/[\d]+\/[a-z]\/)",
    "([\w]+\/[\d]+\/)",
    "([\w]+\/)",
    "([\w]+)",

]

test2 =  "cons1: prod1@app, prod2@app, | cons2: prod3@app, prod4@app"

queue_formats = [ "([\w]+:[\s\w@,]+)" ]

phone_formats = [
    "(\([\d]{3}\)-[\d]{3}-[\d]{4})",
    "(\([\d]{3}\)[\d]{3}-[\d]{4})",
    "(1-[\d]{3}-[\d]{3}-[\d]{4})",

    "(\([\d]{3}\)-[\d]{3}-[\d]{4})",
    "(\([\d]{3}\)[\d]{3}-[\d]{4})",
    "([\d]{3}-[\d]{3}-[\d]{4})",
    "([\d]{3}-[\d]{4})",
]

number = [
    "207-622-2231",
    "622-2231",
    "(774)644-6410"
]



def regex(formats, array):
    result = []
    for item in array:
        for shape in formats:
            found = re.findall(shape, item)
            if found:
                result += found
                break
    return result
print(regex(phone_formats, number))

# print(regex(formats, test))
# print(regex(queue_formats, test2))







