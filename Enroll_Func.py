"""
>>> enroll_large()
[1,2,3]

"""

from Read_test import read_csv
import csv


# raw_data = read_csv("College_Data_score.csv")

def enroll_large(k: int, file: csv):
    # raw_data = read_csv()
    for line in file:
        line[4] = int(line[4])
        line[13] = int(line[13])
        if line[4] <= 250:
            line[13] = line[13] + k * 0
        elif 250 < line[4] <= 600:
            line[13] = line[13] + k * 1
        elif 600 < line[4] <= 2000:
            line[13] = line[13] + k * 2
        else:
            line[13] = line[13] + k * 3
    return file

# def enroll_m():
# raw_data = read_csv()
# for line in raw_data:
# line[4] = int(line[4])
# line[13] = int(line[13])
# if 250 < line[4] <= 600:
# line[13] = line[13] + 1
# else:
# line[13] = line[13]

# def enroll_small():
# raw_data = read_csv()
# for line in raw_data:
# line[4] = int(line[4])
# line[13] = int(line[13])
# if line[4] <= 250:
# line[13] = line[13] + 3
# elif 250 < line[4] <= 600:
# line[13] = line[13] + 2
# elif 600 < line[4] <= 2000:
# line[13] = line[13] + 1
# else:
# line[13] = line[13] + 0
