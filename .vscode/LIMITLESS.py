import tkinter
import tkinter.messagebox
import time

root = tkinter.Tk()
root.title("DA CHECK BOX")
root.geometry("400x200")

def button_click():
    msg = tkinter.messagebox.askokcancel("OK CANCEL", "You pressed the button")

    if msg == True:
        tkinter.messagebox.showinfo("INFO", "Good")
    else:
        tkinter.messagebox.showwarning("INFO", "HOW DARE YOU CANCEL")

btn = tkinter.Button(text = "Don't press me", command = button_click)
btn.pack()

btn_2 = tkinter.Button(text = "Don't press me", command = button_click)
btn.pack()

root.mainloop()

