from tkinter import *
import random
import time
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()

def random_triangle(width,height):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = random.randrange(width)
    y2 = random.randrange(height)
    x3 = random.randrange(width)
    y3 = random.randrange(height)
    colors = ['green','red','blue','orange','yellow',
              'pink','purple','violet','magenta','cyan']
    colour = random.choice(colors)
    canvas.create_polygon(x1,y1,x2,y2,x3,y3,fill=colour)
    tk.update()

for x in range(0,50):
    random_triangle(400,400)
    time.sleep(0.1)
