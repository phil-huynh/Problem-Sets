def best_student_and_score(answer_key):
    score_azami = 0
    score_baz = 0
    score_caris = 0

    azami = {0:"A", 1:"B", 2:"C"}
    baz = {0:"B", 1:"A", 2:"B", 3:"C"}
    caris = {0:"A", 1:"A", 2:"B", 3:"B", 4:"C", 5:"C"}

    i = 0

    while i < len(answer_key):
      if answer_key[i]  == azami.get(i%3):
        score_azami += 1
      if answer_key[i]  == baz.get(i%4):
        score_baz += 1
      if answer_key[i]  == caris.get(i%6):
        score_caris += 1

      i += 1

    highest = max(score_azami, score_baz, score_caris)

    if highest == score_azami:
      return score_azami, "Azami"
    if highest == score_baz:
      return score_baz, "Baz"
    if highest == score_caris:
      return score_caris, "Caris"

student = best_student_and_score("ABBAACCACBCAA")

print(student)