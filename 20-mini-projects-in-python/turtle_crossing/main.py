import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")
screen.onkey(fun=player.move_up, key="w")

game_over = False
while not game_over:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars(player)

    # Detect collision with car
    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.display_game_over()
            game_over = True

    # Detect successful crossing
    if player.is_at_finish_line() and not game_over :
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
