import csv
def read_csv() -> list:
    """
    :return: This function converts the csv file into a big lists with small lists: each of the small lists is
    each lines from the csv file.

    """
    file_handle = open("College_Data_score.csv", 'r')
    data_list = csv.reader(file_handle)
    next(data_list)
    output = list(data_list)
    #print(output)
    return output
