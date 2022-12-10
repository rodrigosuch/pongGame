import turtle as t
BRICK_W = 10
STAMP_SIZE = 20


class Paddle:
    def __init__(self, xposition, Screen, upcallback, downcallback, paddlesize):
        self.paddle = t.Turtle()
        self.paddle.penup()
        self.paddle.setx(xposition)
        self.paddle.color("white")
        self.paddle.shape("square")
        self.paddle.resizemode("user")
        self.paddle.shapesize(BRICK_W / STAMP_SIZE, paddlesize / STAMP_SIZE)
        self.paddle.sety(BRICK_W - BRICK_W / 2)
        self.paddle.setheading(90)
        self.Screen = Screen
        self.Screen.onkey(self.moveup, upcallback)
        self.Screen.onkey(self.movedown, downcallback)
        self.paddlesize = paddlesize

    def moveup(self):
        print(self.Screen.screensize()[1])
        if self.paddle.ycor() < self.Screen.screensize()[1]/2 - self.paddlesize/2:
            self.paddle.forward(BRICK_W*3)

    def movedown(self):
        if self.paddle.ycor() > -self.Screen.screensize()[1]/2 + self.paddlesize/2:
            self.paddle.backward(BRICK_W*3)

    def pos(self):
        return self.paddle.pos()
