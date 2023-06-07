import tkinter
key = 0
def key_pressed(e):
    global key
    key = e.keycode
    print("Hoillo!")

root= tkinter.Tk()
root.title("HMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM")

root.bind("<KeyPress>", key_pressed)
root.mainloop()