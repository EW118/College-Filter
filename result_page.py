from tkinter import *
import pandas as pd
import Sort_Func

res_file = pd.read_csv('rec_scores.csv')
headers = ['College Name', 'Private', 'Apps', 'Accept', 'Enroll', 'Top10perc', 'Outstate', 'PhD', 'S.F.Ratio',
           'perc.alumni', 'Expend', 'Grad.Rate', 'AccpetRate', 'Score']
res_file.to_csv('rec_scores.csv', header=headers, index=False)

ws = Tk()
ws.geometry('600x300')
ws.title('College Filter')

f = ("Times bold", 14)

Label(ws, text=Sort_Func.sort_fun(), padx=20, pady=20, font=f, justify='left').pack()

ws.mainloop()
