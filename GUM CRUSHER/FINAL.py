
import tkinter
import random

index = 0
timer = 0
score = 0
next = 0
hscore = 100
difficulty = 0

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
check = []
for i in range(10):
    board.append([0, 0, 0, 0, 0, 0, 0, 0])
    check.append([0, 0, 0, 0, 0, 0, 0, 0])


def draw_gems():
    cvs.delete("GEMS")
    for y in range(10):
        for x in range(8):
            if board[y][x] > 0:
                cvs.create_image(x * 72 + 60, y *72 + 60, image = img_gems[board[y][x]], tag="GEMS")

def check_gems():
    for y in range(10):
        for x in range(8):
            check[y][x] = board[y][x]
        
    for y in range (10):
        for x in range(1, 7):
            if check[y][x] > 0:
                if check[y][x - 1] == check[y][x] and check[y][x + 1] == check[y][x]:
                    board[y][x - 1] = 7
                    board[y][x] = 7
                    board[y][x + 1] = 7
    
    for y in range (1,9):
        for x in range(8):
            if check[y][x] > 0:
                if check[y - 1][x] == check[y][x] and check[y][x] == check[y + 1][x]:
                    board[y - 1][x] = 7
                    board[y][x] = 7
                    board[y + 1][x] = 7

    for y in range(1, 9):
        for x in range(1, 7):
            if check[y][x] > 0:
                if check[y - 1][x - 1] == check[y][x] and check[y + 1][x + 1] == check[y][x]:
                    board[y - 1][x - 1] = 7
                    board[y][x] = 7
                    board[y + 1][x + 1] = 7
                if check[y + 1][x - 1] == check[y][x] and check[y - 1][x + 1] == check[y][x]:
                    board[y + 1][x - 1] = 7
                    board[y][x] = 7
                    board[y - 1][x + 1] = 7

def sweep_gems():


    num = 0

    for y in range(10):
        for x in range(8):
            if board[y][x] == 7:
                board[y][x] = 0
                num += 1

    return num

def drop_gems():
    flag = False

    for y in range(8, -1, -1):
        for x in range(8):
            if board[y][x] != 0 and  board[y + 1][x] == 0:
                board[y + 1][x] = board[y][x]
                board[y][x] = 0
                flag = True

    return flag

def top_gems():
    for x in range(8):
        if board[0][x] > 0:
            return True
        
    return False

def set_gems():
    for x in range(8):
        board[0][x] = random.randint(0, difficulty)
    

def draw_text(txt, x, y, size, col, tg):

    fnt = ("Agency FB", size, "bold")

    cvs.create_text(x +2, y + 2, text = txt, fill = "black", font = fnt, tag = tg)
    cvs.create_text(x, y, text = txt, fill = col, font = fnt, tag = tg)

def main():
    global index, timer, score, next, hscore, difficulty
    global cursor_x, cursor_y, mouse_c

    if index == 0:
        draw_text("GEM CRUSHER", 312, 240, 60, "violet", "Title")
        cvs.create_rectangle(168, 384, 456, 456, fill = "skyblue", width = 0, tag = "Title")
        draw_text("EZ", 312, 420, 40, "white", "Title")
        cvs.create_rectangle(168, 528, 456, 600, fill = "lightgreen", width = 0, tag = "Title")
        draw_text("Casual", 312, 564, 40, "white", "Title")
        cvs.create_rectangle(168, 672, 456, 744, fill = "dark red", width = 0, tag = "Title")
        draw_text("HARDCORE", 312, 708, 40, "white", "Title")
        index = 1        
        mouse_c = 0

    elif index == 1:
        if mouse_c == 1:
            if 168 <= mouse_x and mouse_x < 456 and 384 <= mouse_y and mouse_y < 456:
                difficulty = 4
            if 168 <= mouse_x and mouse_x < 456 and 528 <= mouse_y and mouse_y < 600:
                difficulty = 5
            if 168 <= mouse_x and mouse_x < 456 and 672 <= mouse_y and mouse_y < 744:
                difficulty = 6
            for y in range(10):
                for x in range(8):
                    board[y][x] = 0
            cursor_x = 0
            cursor_y = 0
            next = 0
            score = 0
            mouse_c = 0

            set_gems()
            draw_gems()

            cvs.delete("Title")
            index = 2

    

    elif index == 2:
        if drop_gems() == False:
            index = 3

        draw_gems()



    elif index == 3:
        check_gems()
        draw_gems()
        index = 4


    elif index == 4:
        sc = sweep_gems()
        score = score + sc * difficulty *  5

        if score > hscore:
            hscore = score

        if sc > 0:
            index = 2
        else:
            if top_gems() == False:
                next = random.randint(1, difficulty)
                index = 5
    
            else:
                index = 6
                timer = 0

        draw_gems()

    elif index == 5:

        if 24 <= mouse_x and mouse_x < 24 + 72 * 8 and 24 <= mouse_y and mouse_y < 24 + 72 * 10:
            cursor_x = int((mouse_x - 24) / 72)
            cursor_y = int((mouse_y - 24) / 72)

            if mouse_c == 1:
                mouse_c = 0
                set_gems()
                board[cursor_y][cursor_x] = next
                next = 0
                index = 2
    
        cvs.delete("Cursor")
        cvs.create_image(cursor_x * 72 + 60, cursor_y * 72 + 60, image = cursor, tag = "Cursor")
        draw_gems()


    elif index == 6:
        timer = timer + 1

        if timer == 1:
            draw_text("GAME OVER", 312, 348, 60, "red", "OVER")
        
        if timer == 50:
            cvs.delete("OVER")
            index = 0

    cvs.delete("INFO")
    draw_text("Score: ", 700, 400, 32, "blue", "INFO")
    draw_text(str(score), 850, 450, 32, "blue", "INFO")
    draw_text("HIGH SCORE: ", 750, 600, 32, "yellow", "INFO")
    draw_text(str(hscore), 850, 650, 32, "yellow", "INFO")
    if next > 0:
        cvs.create_image(738, 156, image = img_gems[next], tag = "INFO")

    root.after(100, main)

root = tkinter.Tk()
root.title("AMOGUS")
root.resizable(False, False)

root.bind("<Motion>", m_move)
root.bind("<ButtonPress>", m_click)

cvs = tkinter.Canvas(root, width = 912, height = 768)
cvs.pack()

g = tkinter.PhotoImage(file = "GUM CRUSHER/pz_bg.png")
cursor = tkinter.PhotoImage(file = "GUM CRUSHER/cursor.png")
img_gems = [
    None,
    tkinter.PhotoImage(file = "GUM CRUSHER/gem1.png"),
    tkinter.PhotoImage(file = "GUM CRUSHER/gem2.png"),
    tkinter.PhotoImage(file = "GUM CRUSHER/gem3.png"),
    tkinter.PhotoImage(file = "GUM CRUSHER/gem4.png"),
    tkinter.PhotoImage(file = "GUM CRUSHER/gem5.png"),
    tkinter.PhotoImage(file = "GUM CRUSHER/gem6.png"),
    tkinter.PhotoImage(file = "GUM CRUSHER/gem_eff.png"),
]   
cvs.create_image(456, 384, image = g)
main()


root.mainloop()    
