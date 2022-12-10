import paddle
from turtle import Screen
from ball import Ball
import time
from score import Score
CANVAS_W = 800
CANVAS_H = 500
PADDLESIZE = 70
screen = Screen()
screen.screensize(CANVAS_W, CANVAS_H)
screen.bgcolor("black")
screen.setup(width=CANVAS_W, height=CANVAS_H, startx=None, starty=None)

paddle1 = paddle.Paddle(CANVAS_W/2 - 50, screen, "Up", "Down", PADDLESIZE)
paddle2 = paddle.Paddle(-CANVAS_W/2 + 50, screen, "w", "s", PADDLESIZE)
ball = Ball(CANVAS_W, CANVAS_H)
score = Score(CANVAS_H/2)
screen.listen()

running = True
while running:
    ball.move()
    if ball.hitwall(CANVAS_H/2):
        ball.bounceinwall()

    paddleGoal = ball.hitinpaddle(paddle1.pos(), 70)
    if paddleGoal == "Hit":
        ball.bounceinpadel()
    elif paddleGoal == "Goal":
        score.scoreleft()
        ball.resetgame()
        time.sleep(2)

    paddleGoal = ball.hitinpaddle(paddle2.pos(), 70)
    if paddleGoal == "Hit":
        ball.bounceinpadel()
    elif paddleGoal == "Goal":
        score.scoreright()
        ball.resetgame()
        time.sleep(2)

    time.sleep(0.01)