from tkinter import *
import SF_ratio_Func
import read_var
import csv

ws = Tk()
ws.geometry('400x300')
ws.title('College Filter')
# ws['bg'] = '#ffbf00'

f = ("Times bold", 14)


def nextPage():
    ws.destroy()
    import page6


def p5_yes():
    a = SF_ratio_Func.stu_fac(1, read_var.read_csv("rec_scores.csv"))
    with open("rec_scores.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(a)

def p5_no():
    b = SF_ratio_Func.stu_fac(0, read_var.read_csv("rec_scores.csv"))
    with open("rec_scores.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(b)


w = Label(ws, text='Do you think the student-faculty ratio is important?', font="50")
w.pack()

Checkbutton_var = IntVar()

Button1 = Checkbutton(ws, text="Yes",
                      variable=Checkbutton_var,
                      onvalue=1,
                      offvalue=0,
                      height=2,
                      width=10,
                      command=lambda: p5_yes())

Button2 = Checkbutton(ws, text="No",
                      variable=Checkbutton_var,
                      onvalue=2,
                      offvalue=1,
                      height=2,
                      width=11,
                      command=lambda: p5_no())




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