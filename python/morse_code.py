    # Remember - you can use the preloaded MORSE_CODE dictionary:
    # For example:
    # MORSE_CODE['.-'] = 'A'
    # MORSE_CODE['--...'] = '7'
    # MORSE_CODE['...-..-'] = '$'

def decode_word(string):
    result = ""
    word = string.strip().split()
    for char in word:
        result += MORSE_CODE[char]
    return result

def decode_morse(morse_code):
    morse_code = morse_code.strip().split("   ")
    message = ""
    for i in range(len(morse_code)):
        morse_code[i] = morse_code[i].strip()
        word = decode_word(morse_code[i])
        if i == 0:
            message += word
        else:
            message += f" {word}"
    return message
