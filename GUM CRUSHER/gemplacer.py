import tkinter
import random

cursor_x = 0
cursor_y = 0
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

board = [
   [0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0]
]

def draw_gems():
    for y in range(10):
        for x in range(8):
            if board[y][x] > 0:
                cvs.create_image(x * 72 + 60, y * 72 + 60, image = img_gems[board[y][x]], tag = "GEMS")

def drop_gems():
    for y in range(8, -1, -1):
        for x in range(8):
            if board[y][x] != 0 and  board[y + 1][x] == 0:
                board[y + 1][x] = board[y][x]
                board[y][x] = 0

def main():
    global cursor_x, cursor_y, mouse_c
    
    drop_gems()

    if 24 <= mouse_x and mouse_x < 24 + 72 * 8 and 24 <= mouse_y and mouse_y < 24 + 72 * 10:
        cursor_x = int((mouse_x - 24) / 72)
        cursor_y = int((mouse_y - 24) / 72)
    
        if mouse_c == 1:
            mouse_c = 0
            board[cursor_y][cursor_x] = random.randint(1,6)
    
    cvs.delete("Cursor")
    cvs.create_image(cursor_x * 72 + 60, cursor_y * 72 + 60, image = cursor, tag = "Cursor")

    cvs.delete("GEMS")
    draw_gems()

    root.after(100, main)

root = tkinter.Tk()
root.title("gem placer")
root.resizable(False, False)

root.bind("<Motion>", m_move)
root.bind("<ButtonPress>", m_click)

cvs = tkinter.Canvas(root, width = 912, height = 768)
cvs.pack()

bg = tkinter.PhotoImage(file = "pz_bg.png")
cursor = tkinter.PhotoImage(file = "cursor.png")
img_gems = [
    None,
    tkinter.PhotoImage(file = "gem1.png"),
    tkinter.PhotoImage(file = "gem2.png"),
    tkinter.PhotoImage(file = "gem3.png"),
    tkinter.PhotoImage(file = "gem4.png"),
    tkinter.PhotoImage(file = "gem5.png"),
    tkinter.PhotoImage(file = "gem6.png"),
    tkinter.PhotoImage(file = "gem_eff.png"),
]   
cvs.create_image(456, 384, image = bg)

main()

root.mainloop()