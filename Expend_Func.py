"""
>>> expend_large(1,file)
[1,2,3]

"""

import csv
import Read_test

file = Read_test.read_csv()


# raw_data = read_csv("College_Data_score.csv")

def expend_large(k: int, file: csv):
    # raw_data = read_csv()
    for line in file:
        line[10] = float(line[10])
        line[13] = float(line[13])
        if line[10] < 6000:
            line[13] = line[13] + k * 0
        elif 6000 <= line[10] < 10000:
            line[13] = line[13] + k * 1
        elif 10000 <= line[10] < 20000:
            line[13] = line[13] + k * 2
        else:
            line[13] = line[13] + k * 3
    return file

# def expend_m(filename: csv):
# raw_data = read_csv(filename)
# for line in raw_data:
# line[10] = int(line[10])
# line[13] = int(line[13])
# if 6000 <= line[10] < 10000:
# line[13] = line[13] + 3
# elif 10000 <= line[10] < 20000 or line[10] < 6000:
# line[13] = line[13] + 2
# else:
# line[13] = line[13] + 0

# def expend_small(filename: csv):
# raw_data = read_csv(filename)
# for line in raw_data:
# line[10] = int(line[10])
# line[13] = int(line[13])
# if line[10] < 6000:
# line[13] = line[13] + 3
# elif 6000 <= line[10] < 10000:
# line[13] = line[13] + 2
# elif 10000 <= line[10] < 20000:
# line[13] = line[13] + 1
# else:
# line[13] = line[13] + 0
