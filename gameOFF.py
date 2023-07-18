from turtle import Turtle
FONT = ("Arial", 12, "normal")

class GameOFF(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.write("Game Ended", True, align="center", font=FONT)
        
    