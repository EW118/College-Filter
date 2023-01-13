from tkinter import *
import Expend_Func
import read_var
import csv

ws = Tk()
ws.geometry('400x300')
ws.title('College Filter')
# ws['bg'] = '#ffbf00'

f = ("Times bold", 14)


def nextPage():
    ws.destroy()
    import result_page


def p7_high():
    a = Expend_Func.expend_large(1, read_var.read_csv("rec_scores.csv"))
    with open("rec_scores.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(a)

def p7_no():
    b = Expend_Func.expend_large(0, read_var.read_csv("rec_scores.csv"))
    with open("rec_scores.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(b)

def p7_low():
    c = Expend_Func.expend_large(-1, read_var.read_csv("rec_scores.csv"))
    with open("rec_scores.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(c)

w = Label(ws, text='Do you want your college expenditure to be?', font="50")
w.pack()

Checkbutton_var = IntVar()

Button1 = Checkbutton(ws, text="High",
                      variable=Checkbutton_var,
                      onvalue=1,
                      offvalue=0,
                      height=2,
                      width=10,
                      command=lambda: p7_high())

Button2 = Checkbutton(ws, text="No Preference",
                      variable=Checkbutton_var,
                      onvalue=2,
                      offvalue=1,
                      height=2,
                      width=11,
                      command=lambda: p7_no())

Button3 = Checkbutton(ws, text="Low",
                      variable=Checkbutton_var,
                      onvalue=3,
                      offvalue=2,
                      height=2,
                      width=10,
                      command=lambda: p7_low())


Button1.pack()
Button2.pack()
Button3.pack()

Button(
    ws,
    text="Sort",
    font=f,
    command=nextPage
).pack(fill=X, expand=TRUE, side=LEFT)

# Button(ws,text="Next Page",font=f,command=prevPage).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()