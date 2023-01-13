import pandas as pd



def sort_fun():
    data_test = pd.read_csv("rec_scores.csv")
    sort_data = data_test.sort_values("Score", axis=0, ascending=False)
    sort_data = sort_data.reset_index()
    sort_data.index = sort_data.index + 1
    sort_data = sort_data[0:5]
    col = ["College Name"]
    return sort_data[col].to_string()
