import tkinter



board = [
    [1, 3, 0, 0, 5, 0, 0, 1],
    [1, 4, 5, 0, 2, 4, 0, 6],
    [0, 0, 6, 3, 0, 4, 0, 3],
    [5, 6, 0, 3, 0, 0, 1, 0],
    [0, 5, 0, 0, 2, 5, 4, 0],
    [4, 3, 0, 5, 5, 0, 1, 3],
    [0, 0, 3, 0, 5, 3, 5, 0],
    [5, 3, 4, 5, 0, 2, 0, 5],
    [0, 0, 3, 5, 4, 5, 0, 4],
    [1, 1, 0, 0, 1, 0, 0, 0]
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
    drop_gems()

    cvs.delete("GEMS")
    draw_gems()

    root.after(100, main)

root = tkinter.Tk()
root.title("2D Array Drop")
root.resizable(False, False)

cvs = tkinter.Canvas(root, width = 912, height = 768)
cvs.pack()

bg = tkinter.PhotoImage(file = "pz_bg.png")
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