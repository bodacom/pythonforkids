from tkinter import *
import random
from tkinter import colorchooser
c = colorchooser.askcolor()
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_polygon(10,10,100,10,100,110,fill="", \
                      outline='black')
canvas.create_polygon(200,10,240,30,120,100,140,120, \
                      fill="",outline='black')

#    def random_rectangle(width,height,fill_color):
#        x1 = random.randrange(width)
#        y1 = random.randrange(height)
#        x2 = x1 + random.randrange(width)
#        y2 = y1 + random.randrange(height)
#        canvas.create_rectangle(x1,y1,x2,y2,fill=fill_color)

#random_rectangle(400,400,'green')
#random_rectangle(400,400,'red')
#random_rectangle(400,400,'blue')
#random_rectangle(400,400,'orange')
#random_rectangle(400,400,'yelow')
#random_rectangle(400,400,'pink')
#random_rectangle(400,400,'purple')
#random_rectangle(400,400,'violet')
#random_rectangle(400,400,'magenta')
#random_rectangle(400,400,'cyan')
random_rectangle(400,400,c[1])