def find_missing_registrant(registrants, finishers):
    finished = {}
    for person in finishers:
        finished[person] = True
    for name in registrants:
        if not finished.get(name):
            return name