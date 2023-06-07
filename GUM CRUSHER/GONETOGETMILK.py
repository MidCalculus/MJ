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

board = []
for i in range(10):
    board.append([0, 0, 0, 0, 0, 0, 0, 0])


def draw_gems():
    for y in range(10):
        for x in range(8):
            if board[y][x] > 0:
                cvs.create_image(x * 72 + 60, y *72 + 60, image = img_gems[board[y][x]], tag="GEMS")

def check_gems():
    for y in range (10):
        for x in range(1, 7):
            if board[y][x] > 0:
                if board[y][x - 1] == board[y][x] and board[y][x + 1] == board[y][x]:
                    board[y][x - 1] = 7
                    board[y][x] = 7
                    board[y][x + 1] = 7

    for y in range (1,9):
        for x in range(8):
            if board[y][x] > 0:
                if board[y - 1][x] == board[y][x] and board[y][x] == board[y + 1][x]:
                    board[y - 1][x] = 7
                    board[y][x] = 7
                    board[y + 1][x] = 7
    

def main():
    global cursor_x, cursor_y, mouse_c

    if 660 <= mouse_x and mouse_x < 840 and 100 <= mouse_y and mouse_y < 160 and mouse_c == 1:
        mouse_c = 0
        check_gems()

    if 24 <= mouse_x and mouse_x < 24 + 72 * 8 and 24 <= mouse_y and mouse_y < 24 + 72 * 10:
        cursor_x = int((mouse_x - 24) / 72)
        cursor_y = int((mouse_y - 24) / 72)
    
        if mouse_c == 1:         
            mouse_c = 0
            board[cursor_y][cursor_x] = random.randint(1,2)
    
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

cvs.create_rectangle(660, 100, 840, 160, fill = "white")
cvs.create_text(750, 130, text = "TEST", fill = "red", font = ("TImes New Roman",))
main()


root.mainloop()    