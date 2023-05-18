def is_baby_word(s):
    if len(s) % 2 != 0:
        return False
    if s[0:int(len(s)/2)] != s[int(len(s)/2): len(s)]:
      return False
    return True

def check(s):
    word = ""
    start = s[0]
    for i, letter in enumerate(reversed(s)):
        if is_baby_word(s[0:(len(s) - i)]):
            temp_w = s[0:(len(s) - i)]
            if len(temp_w) > len(word):
                word = temp_w
            continue
    return word

def baby_talk(s):
    longest_baby_word = ""
    for i, letter in enumerate(s):
        word = check(s[i:])
        if len(word) > len(longest_baby_word):
            longest_baby_word = word
    return len(longest_baby_word)

print(baby_talk("GOOGOOGAGA"))
print(baby_talk("BABABABA"))
print(baby_talk("PTHHPTHHBAGOOGOOGAGABOOOOO"))
print(baby_talk("XYBABABABAXYX"))
print(baby_talk("BABAGOOGOOGOOGOOGOOGOOBA"))
print(baby_talk("NOBABYTALKHERE"))

