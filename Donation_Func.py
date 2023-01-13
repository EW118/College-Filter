"""
>>> donation_large()
[1,2,3]

"""

from Read_test import read_csv
import csv


# raw_data = read_csv("College_Data_score.csv")

def donation_large(k: int, file: csv):
    # raw_data = read_csv()
    for line in file:
        line[9] = float(line[9])
        line[13] = float(line[13])
        if line[9] <= 10:
            line[13] = line[13] + k * 0
        elif 10 < line[9] <= 20:
            line[13] = line[13] + k * 1
        elif 20 < line[9] <= 40:
            line[13] = line[13] + k * 2
        else:
            line[13] = line[13] + k * 3
    return file
