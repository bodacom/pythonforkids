from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, paddle, color, score):
        self.canvas = canvas
        self.paddle = paddle
        self.score = score
        self.id = canvas.create_oval(10,10,25,25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.x = 0
        self.y = 0
        #starts = [-3,-2,-1,1,2,3]
        #random.shuffle(starts)
        #self.x = starts[0]
        #self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Up>', self.start)
        self.hit_bottom = False

    def start(self,evt):
        starts = [-3,-2,-1,1,2,3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False
        
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        paddle_speed = self.paddle.x

        if pos[1] <= 0:
            self.y = 1
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
            self.x = self.x + paddle_speed
            self.score.score = self.score.score + 1
            print (self.score.score)
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3      


class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self,evt):
        self.x = -2

    def turn_right(self,evt):
        self.x = 2
        
    def draw(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

class Score:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.score = 0
        self.id = canvas.create_text(425, 25, text='Score:', font=('Helvetica',10),\
                           fill='green',state='normal')

    def draw(self):
        pass
        
        
#body

tk = Tk()
tk.title("??????")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
game_over_text = canvas.create_text(250, 200, text='Game Over', font=('Helvetica',30),\
                           fill='red',state='hidden')
tk.update()

paddle = Paddle(canvas, 'blue')
score = Score(canvas,'blue')
ball = Ball(canvas, paddle, 'red', score)

while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
        # score draw
    else:
        time.sleep(1)
        canvas.itemconfig(score_text, state='hidden')
        canvas.itemconfig(game_over_text, state='normal')
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
