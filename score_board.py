from turtle import Turtle
FONT = ("Arial", 12, "normal")


class Score(Turtle):
    
    def __init__(self, coordinates):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.ScoreBoardCoordinates = coordinates
        self.score = 0
        self.goto(self.ScoreBoardCoordinates)
        self.write(f"Score: {self.score}", True, align="center", font=FONT)
        
    def UpdateScore(self):
        self.score += 1
        self.clear()
        self.goto(self.ScoreBoardCoordinates)
        self.write(f"Score: {self.score}", True, align="center", font=FONT)