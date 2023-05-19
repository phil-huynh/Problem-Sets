def find_duplicates(some_list):
  duplicates, checker = {}, {}
  for string in some_list:
    if checker.get(string):
      if not duplicates.get(string):
        duplicates[string] = True
    else:
      checker[string] = True
  return list(duplicates)



test_list = ['a', 'b', 'c', 'd', 'b', 'b', 'm', 'n', 'n']
print(find_duplicates(test_list))