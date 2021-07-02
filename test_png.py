from tkinter import *
tk = Tk()
canvas = Canvas(tk, width = 700, height = 700)
canvas.pack()
my_image = PhotoImage(file='/home/bohdan/Pictures/test.png')
canvas.create_image(0,0, anchor=NW, image=my_image)
for
