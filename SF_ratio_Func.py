from Read_test import read_csv
import csv


# raw_data = read_csv("College_Data_score.csv")

def stu_fac(k: int, file: csv):
    # raw_data = read_csv()
    for line in file:
        line[8] = float(line[8])
        line[13] = float(line[13])
        if line[8] <= 10:
            line[13] = line[13] + k * 3
        elif 10 < line[8] <= 15:
            line[13] = line[13] + k * 2
        elif 15 < line[8] <= 20:
            line[13] = line[13] + k * 1
        else:
            line[13] = line[13] + k * 0
    return file
