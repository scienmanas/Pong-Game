from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, corr):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=5, stretch_wid=1 )
        self.speed(0)
        self.penup()
        self.setheading(90)
        self.goto(corr)
        
    def go_up(self):
        self.setheading(90)
        self.forward(20)
    
    def go_down(self):
        self.setheading(270)
        self.forward(20)
        
        