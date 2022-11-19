def move_zeros(numbers):
    print("hello world")
    final = []
    zeros = []

    for number in numbers:
        print("number", number)
        if number == 0:
            zeros.append(number)
            print("here is our zero list: ", zeros)
        else:
            # print("Nope! This number definitely is not zero")
            final.append(number)
    #         print("here is our non-zero list: ", final)
    # print("\nhere is the final list of zeros", zeros)
    # print("\nhere is the final list of non-zeros", final)
    final += zeros

    # print("final is", final)
    return final





print(move_zeros([1,2,3,4,0,6,0,5,4,5,0,0,9]))




























#   zeros = []
#   for i, num in enumerate(array):
#     if num == 0:
#       zeros.insert(0, i)
#   for index in zeros:
#     array.pop(index)
#     array.append(0)
#   return array



