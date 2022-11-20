def phone_words(string):
    if not string:
        return ""
    ref, key = {"0": [" "]}, 2
    letters = "abcdefghijklmnopqrstuvwxyz"
    while letters:
        if key == 7 or key == 9:
            ref[str(key)], letters = letters[:4], letters[4:]
        else:
            ref[str(key)], letters = letters[:3], letters[3:]
        key += 1
    last, string, count, result = string[0], string[1:],  0, ""
    while string:
      num, string = string[0], string[1:]
      if num == last and num != "1":
          if count == len(ref[num]) - 1:
              result += ref[num][count]
              count = 0
          else:
              count += 1
      else:
          if last != "1":
              result += ref[last][count]
          last, count = num, 0
    return result + ref[last][count] if last != "1" else result








print(phone_words("443355555566604466690277733099966688"))   # "hello how are you"
# print(phone_words("55282"))                                  # "kata"
# print(phone_words("44460208337777833777"))                   # "im a tester"
# print(phone_words("22266631339277717777"))                   # "codewars"
# print(phone_words("66885551555"))                            # "null"
# print(phone_words("833998"))                                 # "text"
# print(phone_words("000"))                                    # "   "
# print(phone_words("7999844666166"))                          # "python"
# print(phone_words("55886444833"))                            # "kumite"
# print(phone_words("271755533"))                              # "apple"
# print(phone_words(""))                                       # ""
# print(phone_words("111"))                                    # ""