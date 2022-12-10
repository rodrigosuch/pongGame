from turtle import Turtle
import random
STAMP_SIZE = 20
BALL_SIZE = 10


class Ball:
    def __init__(self, w, h):
        self.ball = Turtle()
        self.ball.penup()
        self.ball.degrees(360)
        self.ball.setheading(45)
        self.ball.color("white")
        self.ball.shape("circle")
        self.ball.resizemode("user")
        self.ball.shapesize(BALL_SIZE / STAMP_SIZE, BALL_SIZE / STAMP_SIZE)
        self.canvasw = w
        self.canvash = h

    def resetgame(self, dist=BALL_SIZE):
        self.ball.setheading(45)
        self.ball.setposition(0,0)

    def move(self, dist=BALL_SIZE):
        self.ball.forward(dist)

    def hitwall(self, wallpos):
        if self.ball.ycor() >= wallpos or \
                self.ball.ycor() <= -wallpos:
            return True
        return False

    def bounceinwall(self):
        if (0 < self.ball.heading() < 90) or \
                (180 < self.ball.heading() < 270):
            self.ball.right(90)
            self.move()
        elif (180 > self.ball.heading() > 90) or \
                (360 > self.ball.heading() > 270):
            self.ball.left(90)
            self.move()

    def hitinpaddle(self, padelpos, size):
        if 0 < self.ball.heading() < 90 or 270 < self.ball.heading() < 360:
            if 0 < padelpos[0] - self.ball.xcor() < BALL_SIZE:
                if self.ball.distance(padelpos[0], padelpos[1]) < size/2:
                    return "Hit"
                else:
                    return "Goal"
        elif 90 < self.ball.heading() < 270:
            if 0 < self.ball.xcor() - padelpos[0] < BALL_SIZE:
                if self.ball.distance(padelpos[0], padelpos[1]) < size/2:
                    return "Hit"
                else:
                    return "Goal"
        return None

    def bounceinpadel(self):
        if (0 < self.ball.heading() < 90) or \
                (180 < self.ball.heading() < 270):
            self.ball.left(90)
            self.move()
        elif (180 > self.ball.heading() > 90) or \
                (360 > self.ball.heading() > 270):
            self.ball.left(-90)
            self.move()
