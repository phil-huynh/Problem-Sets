# https://www.codewars.com/kata/5276c0f3f4bfbd5aae0001ad/train/python

# Write a function that takes a CSV (format shown below) and a sequence of indices, which represents the columns of the CSV, and returns a CSV with only the columns specified in the indices sequence.

# CSV format:
# The CSV passed in will be a string and will have one or more columns, and one or more rows. The CSV will be of size NxM. Each row is separated by a new line character \n. There will be no spaces in the CSV string.

# Example format of passed in CSV: "1,2,3\n4,5,6\n7,8,9\n10,11,12"

# How it would look:

# 1,2,3
# 4,5,6
# 7,8,9
# 10,11,12
# Indices Array info:
# The indices will be zero based, so the first column will be represented as a 0 in the indices sequence.
# All values in the indices sequence will be integers from 0 and up.
# All test cases will have an indices sequence of one or more integers.
# Ignore indices that map to a column that doesn't exist.
# If all the values in the indices array do NOT map to any existing column, return an empty string "".
# The columns of the result must be ordered and not repeated.

# Examples:
# csv, indices                                    => expected
# "1,2,3\n4,5,6", [0, 1]                          => "1,2\n4,5"
# "1,2\n3,4\n5,6", [5, 6, 7]                      => ""
# "a,b,c,d,e\n1,2,3,4,5\nf,g,h,i,j", [1, 3, 5, 7] => "b,d\n2,4\ng,i"


def csv_columns(csv, indices):
    lines = [line.split(',') for line in csv.split('\n')]
    ind = list({i:True for i in indices}.keys())
    ind.sort()
    for i,ln in enumerate(lines):
        new_line = list(filter(lambda a: a != "", [ln[idx] if idx < len(ln) else "" for idx in ind]))
        lines[i] = ",".join(new_line)
        if not new_line:
            return ""
    return "\n".join(lines) if lines else ""