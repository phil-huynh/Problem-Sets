def reverse_prefix(s, letter):
    if letter in s:
        index = s.index(letter)
        rev = []
        [rev.insert(0, char) for char in s[:index+1]]
        s = "".join(rev) + s[index+1:]
    return s


print(reverse_prefix("hackreactor", "c"))

# string = "hello"
# print(string)
# print(reversed(string))