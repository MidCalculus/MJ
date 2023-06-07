from tkinter import *
# Creating a GUI Window
window = Tk()
def from_kg():
    yuan = float(e2_value.get())*6.916
    Euro = float(e2_value.get())*0.9046
    kor_won = float(e2_value.get())*1339.140
    yen = float(e2_value.get())*133.700
    pound = float(e2_value.get())*2.20462
    rupee = float(e2_value.get())*81.698
    t1.delete("1.0",END)
    t1.insert(END, yuan)
    t2.delete("1.0", END)
    t2.insert(END, Euro)
    t3.delete("1.0", END)
    t3.insert(END, kor_won)
    t4.delete("1.0",END)
    t4.insert(END, yen)
    t5.delete("1.0", END)
    t5.insert(END, pound)
    t6.delete("1.0", END)
    t6.insert(END, rupee)

e1 = Label(window, text="Input the $$$")
e2_value = StringVar()
e2 = Entry(window, textvariable=e2_value)
e3 = Label(window, text="Yuan")
e4 = Label(window, text="Euro")
e5 = Label(window, text="Kor won")
e6 = Label(window, text="Yen")
e7 = Label(window, text="Pound")
e8 = Label(window, text="rupee")

t1 = Text(window, height=5, width=30)
t2 = Text(window, height=5, width=30)
t3 = Text(window, height=5, width=30)
t4 = Text(window, height=5, width=30)
t5 = Text(window, height=5, width=30)
t6 = Text(window, height=5, width=30)


b1 = Button(window, text="Convert", command=from_kg)

e1.grid(row=0, column=0)
e2.grid(row=0, column=1)
e3.grid(row=1, column=0)
e4.grid(row=1, column=1)
e5.grid(row=1, column=2)
e6.grid(row=1, column=3)
e7.grid(row=1, column=4)
e8.grid(row=1, column=5)
t1.grid(row=2, column=0)
t2.grid(row=2, column=1)
t3.grid(row=2, column=2)
t4.grid(row=2, column=3)
t5.grid(row=2, column=4)
t6.grid(row=2, column=5)
b1.grid(row=0, column=2)

window.mainloop()