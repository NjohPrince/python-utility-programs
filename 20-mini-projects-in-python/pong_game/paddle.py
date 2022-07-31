from turtle import Turtle

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Paddle(Turtle):
    def __init__(self, **kwargs):
        super().__init__(shape="square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=3, stretch_len=1)
        self.x_cor = kwargs.get("x_cor", 0)
        self.y_cor = kwargs.get("y_cor", 0)
        self.goto(self.x_cor, self.y_cor)
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
