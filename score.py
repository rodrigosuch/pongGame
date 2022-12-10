from turtle import Turtle

class Score:
    def __init__(self, ypos):
        self.score = Turtle()
        self.score.penup()
        self.score.degrees(360)
        self.score.color("white")
        self.score.sety(ypos)
        self.score.hideturtle()
        self.score.write("0 X 0", True, align="center", font=('Arial', 30, 'normal'))
        self.left = 0
        self.right = 0

    def scoreleft(self):
        self.left += 1
        text = '%d X %d' %(self.left, self.right)
        self.score.clear()
        self.score.setx(0)
        self.score.write(text, True, align="center", font=('Arial', 30, 'normal'))

    def scoreright(self):
        self.right += 1
        text = '%d X %d' %(self.left, self.right)
        self.score.clear()
        self.score.setx(0)
        self.score.write(text, True, align="center", font=('Arial', 30, 'normal'))
