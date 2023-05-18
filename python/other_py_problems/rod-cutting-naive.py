values = {
  1: 1,
  2: 2,
  3: 5,
  4: 4,
  5: 8,
}

extra_memory = {}

def max_cut_stock(rod_length, values):
    max_value = values.get(rod_length, 0)

    if extra_memory.get(rod_length):
        max_value = extra_memory[rod_length]
        print(f"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX Cached value  -----> {max_value}")
    else:
        for cut_length in range(1, rod_length):
            cut_value = values.get(cut_length, 0)
            remaining_length = rod_length - cut_length
            max_remaining_value = max_cut_stock(remaining_length, values)

            if cut_value + max_remaining_value > max_value:
                max_value = cut_value + max_remaining_value
            print(f"{cut_value + max_remaining_value: > 3} cut {rod_length} into {cut_length} and {remaining_length}")
        extra_memory[rod_length] = max_value
    print(f"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Solution found  -----> {max_value}")
    return max_value
max_cut_stock(7, values)
max_cut_stock(10, values)
max_cut_stock(15, values)
max_cut_stock(10, values)
max_cut_stock(20, values)
print("EXTRA MEMORY CONTAINS", extra_memory)