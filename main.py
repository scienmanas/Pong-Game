import random
from turtle import Turtle, Screen
import time 
from paddle import Paddle
from ball import Ball
from score_board import Score
from gameOFF import GameOFF

def GAMEOFF():
    global is_game_on
    is_game_on = False
    gameoff = GameOFF()
    

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height= 700)
screen.title("Pong Game")

# Creating paddle 

screen.tracer(0)
r_paddle = Paddle((370,0))
l_paddle = Paddle((-370,0))

choices = [-1,1]
ball = Ball(random.choice(choices),random.choice(choices))

score_r = Score((200,330))
score_l = Score((-200,330))

screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")
screen.onkeypress(GAMEOFF, "e")

is_game_on = True


while is_game_on:
    screen.update()
    time.sleep(0.1)
    if ball.ycor() == 340 or ball.ycor() == -340:
        ball.y_change()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() > -340:
        ball.x_change()
    if ball.xcor() >= 400 :
        ball.hideturtle()
        ball = Ball(-1,random.choice(choices))
        score_l.UpdateScore()
    if ball.xcor() <= -400 :
        ball.hideturtle()
        ball = Ball(1,random.choice(choices))
        score_r.UpdateScore()
    ball.Move()






screen.exitonclick()