
import tkinter
import random

root = tkinter.Tk()
root.title("The extremely trustwory online fortune teller")
root.resizable(False, False)
canvas = tkinter.Canvas(root, width = 800, height = 600)
canvas.pack()

picture = tkinter.PhotoImage(file = "tk1_bg.png")
canvas.create_image(400, 300, image = picture)
picture_2 = tkinter.PhotoImage(file = "tk1_horo.png")
canvas.create_image(180, 446, image = picture_2)


label = tkinter.Label(root, text = "???", font = ("Comic Sans,", 80), bg = "white" )
label.place(x = 400, y = 160)


def button_press():
    list = ["Lucky", "So-So", "UnLucky", "SECRET"]
    label["font"] = ("Courier New", 50 )
    label["text"] = random.choice(list)
    label.update


button = tkinter.Button(root, text = "Test Your Fortune!", font = ("Times New Roman", 36),fg = "skyblue", command = button_press)
button.place(x = 370, y = 400)


root.mainloop()