import tkinter

from pygame import BIG_ENDIAN

cursor_x = 0
cursor_y = 0
mouse_x = 0
mouse_y = 0

def m_move(e):
    global mouse_x, mouse_y
    mouse_x = e.x
    mouse_y = e.y

def main():
    global cursor_x, cursor_y

    if 24 <= mouse_x and mouse_x < 24 + 72 * 8 and 24 <= mouse_y and mouse_y < 24 + 72 * 10:
        cursor_x = int((mouse_x - 24) / 72)
        cursor_y = int((mouse_y - 24) / 72)

    cvs.delete("Cursor")
    cvs.create_image(cursor_x * 72 + 60, cursor_y * 72 + 60, image = cursor, tag = "Cursor")

    root.after(100, main)

root = tkinter.Tk()
root.title("Cursor moving")
root.resizable(False, False)

root.bind("<Motion>", m_move)

cvs = tkinter.Canvas(root, width = 912, height = 768)
cvs.pack()

bg = tkinter.PhotoImage(file = "pz_bg.png")
cursor = tkinter.PhotoImage(file = "cursor.png")
cvs.create_image(456, 384, image = bg)

main()

root.mainloop()






























































































