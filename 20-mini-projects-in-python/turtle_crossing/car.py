from random import choice
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
END_OF_SCREEN = 300


class Car(Turtle):
    def __init__(self, y):
        super().__init__("square")
        self.penup()
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(choice(COLORS))
        self.setposition(END_OF_SCREEN, y)

    def move(self, move_distance):
        self.backward(move_distance)
