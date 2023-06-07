import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.title("DA CHECK BOX")
root.geometry("400x200")

def button_click():
    tkinter.messagebox.showwarning("Bruh", "Didn't you listen??? >:(")

btn = tkinter.Button(text = "Don't press me", command = button_click)
btn.pack()

btn_2 = tkinter.Button(text = "Don't press me", command = button_click)
btn.pack()

root.mainloop()

