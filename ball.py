from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self, X_COOR, Y_COOR):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.goto(0,0)
        self.speed(0)
        self.X_SYMBOL = X_COOR
        self.Y_SYMBOL = Y_COOR

    def x_change(self):
        self.X_SYMBOL = self.X_SYMBOL*-1
    
    def y_change(self):
        self.Y_SYMBOL = self.Y_SYMBOL*-1
        
    def Move(self):
        x = self.xcor() + 10*self.X_SYMBOL
        y = self.ycor() + 10*self.Y_SYMBOL
        self.goto(x,y)