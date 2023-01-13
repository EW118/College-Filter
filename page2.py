from tkinter import *
import tkinter
import Accept_Func
import Read_test
import read_var
import csv

ws = Tk()
ws.geometry('400x300')
ws.title('College Filter')
# ws['bg'] = '#ffbf00'

f = ("Times bold", 14)

# file = Read_test.read_csv()

def nextPage():
    ws.destroy()
    import page3

def p2_low():
    a = Accept_Func.accept_hard(1, read_var.read_csv("rec_scores.csv"))
    with open("rec_scores.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(a)

def p2_no():
    b = Accept_Func.accept_hard(0, read_var.read_csv("rec_scores.csv"))
    with open("rec_scores.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(b)

def p2_high():
    c = Accept_Func.accept_hard(-1, read_var.read_csv("rec_scores.csv"))
    with open("rec_scores.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(c)

# def prevPage():
    # ws.destroy()
    # import page1

w = Label(ws, text='Do you want the acceptance rate to be?', font="50")
w.pack()

Checkbutton_var = IntVar()

Button1 = Checkbutton(ws, text="Low",
                      variable=Checkbutton_var,
                      onvalue=1,
                      offvalue=0,
                      height=2,
                      width=10,
                      command=lambda: p2_low())

Button2 = Checkbutton(ws, text="No preference",
                      variable=Checkbutton_var,
                      onvalue=2,
                      offvalue=1,
                      height=2,
                      width=11,
                      command=lambda: p2_no())

Button3 = Checkbutton(ws, text="High",
                      variable=Checkbutton_var,
                      onvalue=3,
                      offvalue=2,
                      height=2,
                      width=10,
                      command=lambda: p2_high())



Button1.pack()
Button2.pack()
Button3.pack()
# Label(ws,text="This is Second page",padx=20,pady=20,bg='#ffbf00',font=f).pack(expand=True, fill=BOTH)

Button(
    ws,
    text="Next Page",
    font=f,
    command=nextPage
).pack(fill=X, expand=TRUE, side=LEFT)

# Button(ws,text="Next Page",font=f,command=prevPage).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()
