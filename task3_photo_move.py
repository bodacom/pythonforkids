from tkinter import *
import time
tk = Tk()
canvas = Canvas(tk, width = 700, height = 700)
canvas.pack()
my_image = PhotoImage(file='/home/bohdan/Pictures/test.png')
canvas.create_image(0,0, anchor=NW, image=my_image)
for a in range(0,10):
    for x in range(0,10):
        canvas.move(1,5,0)
        tk.update()
        time.sleep(0.05)
    for x in range(0,10):
        canvas.move(1,-5,0)
        tk.update()
        time.sleep(0.05)
