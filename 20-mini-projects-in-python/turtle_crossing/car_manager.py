from random import randint

from car import Car

MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager:
    def __init__(self):
        self.move_distance = MOVE_DISTANCE
        # self.move_increment = MOVE_INCREMENT
        self.cars = []

    def move_cars(self, player):
        for car in self.cars:
            car.move(self.move_distance)
            if car.xcor() < -300:
                car.color("white")
                self.cars.remove(car)

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            car_y = randint(-250, 260)
            new_car = Car(car_y)
            self.cars.append(new_car)

    def level_up(self):
        self.move_distance += MOVE_INCREMENT
