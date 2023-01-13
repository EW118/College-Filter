from tkinter import *

import Read_test

import Enroll_Func

import csv

ws = Tk()
ws.geometry('400x300')
ws.title('College Filter')
# ws['bg'] = '#5d8a82'

f = ("Times bold", 14)
file = Read_test.read_csv()


def nextPage():
    ws.destroy()
    import page2


def p1_large():
    a = Enroll_Func.enroll_large(1, file)
    with open("rec_scores.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(a)


def p1_no():
    b = Enroll_Func.enroll_large(0, file)
    with open("rec_scores.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(b)


def p1_small():
    c = Enroll_Func.enroll_large(-1, file)
    with open("rec_scores.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(c)


# def prevPage():
#  ws.destroy()
#  import page3


# Label(ws,text="This is First page",padx=20,pady=20,bg='#5d8a82',font=f).pack(expand=True, fill=BOTH)
w = Label(ws, text='How do you expect the school size?', font="50")
w.pack()

Checkbutton_var = IntVar()

Button1 = Checkbutton(ws, text="Large",
                      variable=Checkbutton_var,
                      onvalue=1,
                      offvalue=0,
                      height=2,
                      width=10,
                      command=lambda: p1_large())

Button2 = Checkbutton(ws, text="No preference",
                      variable=Checkbutton_var,
                      onvalue=2,
                      offvalue=1,
                      height=2,
                      width=11,
                      command=lambda: p1_no())

Button3 = Checkbutton(ws, text="Small",
                      variable=Checkbutton_var,
                      onvalue=3,
                      offvalue=2,
                      height=2,
                      width=10,
                      command=lambda: p1_small())

Button1.pack()
Button2.pack()
Button3.pack()

Button(
    ws,
    text="Next Page",
    font=f,
    command=nextPage
).pack(fill=X, expand=TRUE, side=LEFT)

# Button(ws,text="Next Page",font=f,command=prevPage.pack(fill=X, expand=TRUE, side=LEFT)

mainloop()
if __name__ == "__main__":
    nextPage()