from turtle import Turtle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__(shape="square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=3, stretch_len=1)
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.goto(x_cor, y_cor)
        self.speed(0)

    def go_up(self):
        y = self.ycor()
        if y > (SCREEN_HEIGHT / 2 - 30):
            self.sety(SCREEN_HEIGHT / 2 - 20)
        else:
            y = self.ycor()
            y += 20
            self.sety(y)

    def go_down(self):
        y = self.ycor()
        if y < ((SCREEN_HEIGHT / 2 - 35) * -1):
            self.sety((SCREEN_HEIGHT / 2 - 25) * -1)
        else:
            y = self.ycor()
            y -= 20
            self.sety(y)
