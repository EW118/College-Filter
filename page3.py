from tkinter import *
import Top_10_perc_Func
import csv
import read_var

ws = Tk()
ws.geometry('400x300')
ws.title('College Filter')
# ws['bg'] = '#ffbf00'

f = ("Times bold", 14)


def nextPage():
    ws.destroy()
    import page4

def p3_high():
    a = Top_10_perc_Func.top_10_perc_more(1, read_var.read_csv("rec_scores.csv"))
    with open("rec_scores.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(a)

def p3_no():
    b = Top_10_perc_Func.top_10_perc_more(0, read_var.read_csv("rec_scores.csv"))
    with open("rec_scores.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(b)

def p3_low():
    c = Top_10_perc_Func.top_10_perc_more(-1, read_var.read_csv("rec_scores.csv"))
    with open("rec_scores.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(c)

# def prevPage():
  #  ws.destroy()
   # import page2


w = Label(ws, text='Do you want your academic rigor to be?', font="50")
w.pack()

Checkbutton_var = IntVar()

Button1 = Checkbutton(ws, text="High",
                      variable=Checkbutton_var,
                      onvalue=1,
                      offvalue=0,
                      height=2,
                      width=10,
                      command=lambda: p3_high())

Button2 = Checkbutton(ws, text="No preference",
                      variable=Checkbutton_var,
                      onvalue=2,
                      offvalue=1,
                      height=2,
                      width=11,
                      command=lambda: p3_no())

Button3 = Checkbutton(ws, text="Low",
                      variable=Checkbutton_var,
                      onvalue=3,
                      offvalue=2,
                      height=2,
                      width=10,
                      command=lambda: p3_low())



Button1.pack()
Button2.pack()
Button3.pack()

Button(
    ws,
    text="Next Page",
    font=f,
    command=nextPage
).pack(fill=X, expand=TRUE, side=LEFT)

# Button(ws,text="Next Page",font=f,command=prevPage).pack(fill=X, expand=TRUE, side=LEFT)

ws.mainloop()
