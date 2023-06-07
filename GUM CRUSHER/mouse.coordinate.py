import tkinter

mouse_x = 0
mouse_y = 0
mouse_c = 0

def m_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def m_click(e):
    global mouse_c
    mouse_c = 1

def m_release(E):
    global mouse_c
    mouse_c = 0

def main():
    fnt = ("arial", 20)
    txt = "mouse({},{}){}".format(mouse_x, mouse_y, mouse_c)

    cvs.delete("Test")
    cvs.create_text(400, 300, text = txt, fill = "black", font = fnt, tag = "Test")

    root.after(100, main)

root = tkinter.Tk()
root.title("Mouse INpput")
root.resizable(False, False)
root.bind("<Motion>", m_move)
root.bind("<ButtonPress>", m_click)
root.bind("ButtonRelease>", m_release)

cvs = tkinter.Canvas(root, width = 800, height = 600)
cvs.pack()

main()

root.mainloop()



















































































