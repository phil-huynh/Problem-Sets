def calculate_num_letters(num_pushes):
    num_x = 0
    num_o = 0
    output = []
    for i in range(num_pushes):
        if i == 0:
            output.append("X")
        else:
            for i, char in enumerate(output):
                if char == "X":
                    output[i] = "O"
                if char == "O":
                    output[i] = "OX"
            output = "".join(output)
            storage  = []
            [storage.append(letter) for letter in output]
            output = storage
    for letter in output:
        if letter == "X":
            num_x += 1
        if letter == "O":
            num_o += 1

    return num_x, num_o