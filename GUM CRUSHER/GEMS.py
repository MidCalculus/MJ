import tkinter

board = [
    [1, 3, 3, 1, 5, 4, 3, 1],
    [1, 4, 5, 6, 2, 4, 5, 6],
    [3, 5, 6, 2, 3, 4, 5, 3],
    [5, 6, 1, 3, 6, 5, 1, 3],
    [3, 5, 6, 1, 2, 3, 4, 5],
    [4, 3, 2, 1, 5, 6, 1, 3],
    [3, 1, 3, 4, 5, 6, 5, 3],
    [5, 3, 4, 5, 1, 2, 3, 5],
    [2, 1, 3, 5, 4, 5, 6, 4],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

def draw_gems():
    for y in range(10):
        for x in range(8):
            if board[y][x] > 0:
                cvs.create_image(x * 72 + 60, y *72 + 60, image = img_gems[board[y][x]])

root = tkinter.Tk()
root.title("2D Array")
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

draw_gems()

root.mainloop()

