import tkinter
import tkinter.messagebox
import sys

def button_click():
    check = 0
    mbti = ""

    while True:
        for i in range(4):
            if bvar1[i].get() == True and bvar2[i].get() == True:
                text.delete("1.0", tkinter.END)
                text.insert("1.0", "Check only one between two choices.")
                return
            if bvar1[i].get() == True or bvar2[i].get() == True:
                check += 1

        if check >= 4:
            for j in range(4):
                if j == 0:
                    if bvar1[j].get() == True:
                        mbti += "E"
                    else:
                        mbti += "I"
                if j == 1:
                    if bvar1[j].get() == True:
                        mbti += "S"
                    else:
                        mbti += "N"
                if j == 2:
                    if bvar1[j].get() == True:
                        mbti += "F"
                    else:
                        mbti += "T"
                if j == 3:
                    if bvar1[j].get() == True:
                        mbti += "J"
                    else:
                        mbti += "P"

        break

    text.delete("1.0", tkinter.END)
    text.insert("1.0", "Your MBTI is: " + mbti)

root = tkinter.Tk()
root.title("DA CHECK BOX")
root.geometry("800x600")

canvas = tkinter.Canvas(root, width = 800, height = 600, bg = "Dark red")
canvas.pack()

picture = tkinter.PhotoImage(file = "something.py/tk2_bg.png")
canvas.create_image(400,300, image = picture)

text = tkinter.Text(width = 40, height = 5, font = ("Times New Romans", 16))
text.place(x = 320, y = 30)

label = tkinter.Label(root, text = "How do you react when you are facing a problem?", font = ("TImes New Romans,", 16))
label.place(x = 300, y = 150)

button = tkinter.Button(root, text = "See Results", font = ("Comic Sans MS", 20), command = button_click)
button.place(x = 500, y = 450)

bvar1 = [None]* 4
ckbt1 = [None] * 4

ITEM1 = [
    "Become Talkative",
    "I guess it could happen",
    """I dont get it
    but I can feel you""",
    "Just do it"
]

for i in range(4):
    bvar1[i] = tkinter.BooleanVar()
    bvar1[i].set(False)
    ckbt1[i] = tkinter.Checkbutton(text = ITEM1[i], font = ("Courier Ner", 9), variable = bvar1[i])
    ckbt1[i].place(x = 320, y = 200 + 70 * i)

bvar2 = [None]* 4
ckbt2 = [None] * 4

ITEM2 = [
    "Think too much",
    "How did it happen?",
    "I need to undesratand first",
    "What should I do first?"
]

for i in range(4):
    bvar2[i] = tkinter.BooleanVar()
    bvar2[i].set(False)
    ckbt2[i] = tkinter.Checkbutton(text = ITEM2[i], font = ("Courier Ner", 9), variable = bvar2[i])
    ckbt2[i].place(x = 550, y = 200 + 70 * i)

root.mainloop()