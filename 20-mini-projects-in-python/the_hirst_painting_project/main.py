from random import choice
from turtle import Turtle, Screen

rgb_colors = [(201, 167, 134), (236, 243, 249), (144, 51, 99), (163, 167, 41), (238, 71, 125), (237, 83, 61),
              (17, 140, 64), (241, 221, 67), (225, 118, 163), (10, 142, 179), (67, 198, 219), (157, 59, 53),
              (23, 169, 129), (32, 187, 202), (127, 188, 163), (107, 42, 88), (248, 231, 0), (236, 163, 188),
              (244, 168, 155), (141, 214, 224), (145, 218, 199), (136, 39, 34), (79, 36, 73), (3, 114, 36)]
"""
colors = colorgram.extract("image.jpg", 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
"""
tim = Turtle()
tim.hideturtle()
tim.penup()
screen = Screen()
screen.colormode(255)

tim.setheading(225)
tim.forward(350)
tim.setheading(0)


def left_to_right(number_of_dots):
    tim.speed("fastest")
    for dot_count in range(1, number_of_dots + 1):
        tim.pencolor(choice(rgb_colors))
        tim.dot(20)
        tim.forward(50)
        if dot_count % 10 == 0:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)


left_to_right(100)
screen.exitonclick()
