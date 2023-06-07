from pprint import pprint

unsortedQueue = [
  { "taskId": 2, "isUrgent": True, "dueAt": 7, "patientId": "C", "providerId": "Z" },
  { "taskId": 5, "isUrgent": False, "dueAt": 8, "patientId": "B", "providerId": "Z" },
  { "taskId": 6, "isUrgent": False, "dueAt": 9, "patientId": "B", "providerId": "Y" },
  { "taskId": 1, "isUrgent": True, "dueAt": 6, "patientId": "A", "providerId": "X" },
  { "taskId": 7, "isUrgent": False, "dueAt": 5, "patientId": "C", "providerId": "X" },
  { "taskId": 4, "isUrgent": False, "dueAt": 4, "patientId": "B", "providerId": "Y" },
  { "taskId": 3, "isUrgent": False, "dueAt": 3, "patientId": "B", "providerId": "Z" }
]


def next_due(queue):
    due_first = queue[0]["patientId"]
    time = queue[0]["dueAt"]
    for patient in queue:
        if patient["dueAt"] < time:
            time = patient["dueAt"]
            due_first = patient["patientId"]
    return due_first


def patient(group, patient):
    current_patient = list(filter(lambda a: a["patientId"] == patient, group))
    current_patient.sort(key=lambda a: a["dueAt"])
    return current_patient


def remove_patient(queue, patient):
    return (list(filter(lambda a: a["patientId"] != patient, queue)))


def schedule(queue):
    final_list = []
    while queue:
        next_patient = next_due(queue)
        final_list += patient(queue, next_patient)
        queue = remove_patient(queue, next_patient)
    return final_list


def final_schedule(queue):
    initial_schedule = schedule(queue)
    urgent, not_urgent = [], []
    for entry in initial_schedule:
        urgent.append(entry) if entry["isUrgent"] else not_urgent.append(entry)
    urgent.sort(key=lambda a: a["dueAt"])
    return urgent + not_urgent



print(final_schedule(unsortedQueue))

