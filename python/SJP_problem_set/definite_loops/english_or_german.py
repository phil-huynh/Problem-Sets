def language(text):
    english_check = text.split("ie")
    german_check = text.split("ei")

    if len(english_check) == len(german_check):
        return "Maybe French?"
    if len(english_check) > len(german_check):
        return "English"
    if len(english_check) < len(german_check):
        return "German"