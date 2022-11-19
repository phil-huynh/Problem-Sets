def grade_scantron(submission, answer_key):
    score = 0
    for i, answer in enumerate(answer_key):
        if answer == submission[i]:
            score += 1
    return score