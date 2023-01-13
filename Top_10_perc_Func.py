"""
>>> top_10_perc_more()
[1,2,3]

"""

from Read_test import read_csv
import csv


# raw_data = read_csv("College_Data_score.csv")

def top_10_perc_more(k: int, file: csv):
    # raw_data = read_csv()
    for line in file:
        line[5] = float(line[5])
        line[13] = float(line[13])
        if line[5] <= 15:
            line[13] = line[13] + k * 0
        elif 15 < line[5] <= 35:
            line[13] = line[13] + k * 1
        elif 35 < line[5] <= 45:
            line[13] = line[13] + k * 2
        else:
            line[13] = line[13] + k * 3
    return file
