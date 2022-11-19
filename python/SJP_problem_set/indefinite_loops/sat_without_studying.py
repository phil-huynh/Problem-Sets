def best_student_and_score(answer_key):
    score_azami = 0
    score_baz = 0
    score_caris = 0

    azami = ["A", "B", "C"]
    baz = ["B", "A", "B", "C"]
    caris = ["A", "A", "C", "C", "B", "B"]

    for i, answer in enumerate(answer_key):
      if answer == azami[i%3]:
        score_azami += 1
      if answer == baz[i%4]:
        score_baz += 1
      if answer == caris[i%6]:
        score_caris += 1

    highest = max(score_azami, score_baz, score_caris)

    if highest == score_azami:
      return score_azami, "Azami"
    if highest == score_baz:
      return score_baz, "Baz"
    if highest == score_caris:
      return score_caris, "Caris"