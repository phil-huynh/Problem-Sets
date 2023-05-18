def string_expansion(s):
    has_num = False
    multiplier = None
    final = ""
    for i, char in enumerate(s):
        if not has_num and not char.isdigit():
            final += char
        if char.isdigit() and i != len(s) - 1 and not s[i + 1].isdigit():
            has_num = True
            multiplier = int(char)
        if has_num and not char.isdigit():
            final += multiplier * char
    return final

print(string_expansion("3D2a5d2f"))