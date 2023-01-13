"""
>>> accept_hard(1,file)
[1,2,3]

"""


from Read_test import read_csv
import csv
import Read_test

file = Read_test.read_csv()

def accept_hard(k: int, file: csv):
    # raw_data = read_csv()

    for line in file:
        line[12] = float(line[12])
        line[13] = float(line[13])

        if line[12] <= 0.55:
            line[13] = line[13] + k * 3
        elif 0.55 < line[12] <= 0.7:
            line[13] = line[13] + k * 2
        elif 0.7 < line[12] <= 0.83:
            line[13] = line[13] + k * 1
        else:
            line[13] = line[13] + k * 0
    return file

# def accept_m(filename: csv) -> list:

# raw_data = read_csv(filename)

# for line in raw_data:
# line[12] = float(line[12])
# line[13] = float(line[13])

# if 0.7 < line[12] <= 0.83:
# line[13] = line[13] + 3
# elif 0.55 < line[12] <= 0.7:
# line[13] = line[13] + 2
# elif 0.83 < line[12] <= 1.00:
# line[13] = line[13] + 2
# else:
# line[13] = line[13] + 0
# return raw_data


# def accept_easy(filename: csv) -> list:

# raw_data = read_csv(filename)

# for line in raw_data:
# line[12] = float(line[12])
# line[13] = float(line[13])

# if line[12] <= 0.55:
# line[13] = line[13] + 0
# elif 0.55 < line[12] <= 0.7:
# line[13] = line[13] + 1
# elif 0.7 < line[12] <= 0.83:
# line[13] = line[13] + 2
# else:
# line[13] = line[13] + 3
# return raw_data
