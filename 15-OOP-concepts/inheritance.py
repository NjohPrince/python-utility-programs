# Inheritance

# Inheritance allows us to define a class that inherits all the methods and
# properties from another class. Parent class is the class being inherited
# from, also called base class. Child class is the class that inherits
# from another class, also called derived class.

class Car():
    def category(self):
        print("Ferrari")

    def color(self):
        print("Color: Red")


class BadCars(Car):
    pass  # no properties or methods


car_obj = BadCars()

car_obj.category()  # Ferrari
