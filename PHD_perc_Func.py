"""
>>> phd_perc_large()
[1,2,3]

"""

from Read_test import read_csv
import csv


# raw_data = read_csv("College_Data_score.csv")

def phd_perc_large(k: int, file: csv):
    # raw_data = read_csv()
    for line in file:
        line[7] = float(line[7])
        line[13] = float(line[13])
        if line[7] <= 50:
            line[13] = line[13] + k * 0
        elif 50 < line[7] <= 70:
            line[13] = line[13] + k * 1
        elif 70 < line[7] <= 90:
            line[13] = line[13] + k * 2
        else:
            line[13] = line[13] + k * 3
    return file
