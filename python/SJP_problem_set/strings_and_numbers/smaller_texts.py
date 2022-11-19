def count_words(message):
    message = message.split()
    if len(message) <= 30:
        return True
    return False