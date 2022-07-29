from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(-285, 250)
        self.update_scoreboard()

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level} High Score: {self.high_score}", align="left", font=FONT)

    def display_game_over(self):
        if self.level > self.high_score:
            with open("data.txt", mode="w") as data:
                data.write(f"{self.level}")
        self.update_scoreboard()
        self.high_score = self.level
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
