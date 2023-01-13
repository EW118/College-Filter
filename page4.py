from tkinter import *
import PHD_perc_Func
import read_var
import csv

ws = Tk()
ws.geometry('400x300')
ws.title('College Filter')
# ws['bg'] = '#ffbf00'

f = ("Times bold", 14)


def nextPage():
    ws.destroy()
    import page5


def p4_yes():
    a = PHD_perc_Func.phd_perc_large(1, read_var.read_csv("rec_scores.csv"))
    with open("rec_scores.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(a)

def p4_no():
    b = PHD_perc_Func.phd_perc_large(0, read_var.read_csv("rec_scores.csv"))
    with open("rec_scores.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(b)


w = Label(ws, text='Do you think the quality of teachers is important?', font="50")
w.pack()

Checkbutton_var = IntVar()

Button1 = Checkbutton(ws, text="Yes",
                      variable=Checkbutton_var,
                      onvalue=1,
                      offvalue=0,
                      height=2,
                      width=10,
                      command=lambda: p4_yes())

Button2 = Checkbutton(ws, text="No",
                      variable=Checkbutton_var,
                      onvalue=2,
                      offvalue=1,
                      height=2,
                      width=11,
                      command=lambda: p4_no())




Button1.pack()
Button2.pack()

Button(
    ws,
    text="Next Page",
    font=f,
    command=nextPage
).pack(fill=X, expand=TRUE, side=LEFT)

# Button(ws,text="Next Page",font=f,command=prevPage).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()
