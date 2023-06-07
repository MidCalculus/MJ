
import tkinter

root = tkinter.Tk()
root.title("MY first input")
root.geometry("400x200")

def confrim():
    text.insert(tkinter.END, "END OF THE LINE BUDDY")


button = tkinter.Button(text = "Message", command = confrim)
button.place( x = 20, y = 80)
button.pack()

text = tkinter.Text()
text.place(x = 20, y = 50, width = 360, height = 120)

root.mainloop()