# Polymorphism

# Polymorphism defines the ability to take different forms.
# Polymorphism in Python allows us to define methods in
# the child class with the same name as defined in
# their parent class.

# Polymorphism using functions and objects

class Car():
    def category(self):
        print("Ferrari")

    def color(self):
        print("Color: Red")


class Person():
    def category(self):
        print("Male")

    def color(self):
        print("Color: Black")


def func(obj):
    obj.category()
    obj.color()


car_obj = Car()
person_obj = Person()
func(car_obj)
func(person_obj)

# Polymprphism in with methods of classes

print("\n")

car_obj = Car()
person_obj = Person()
for elements in (car_obj, person_obj):
    elements.category()
    elements.color()

# Polymprphism in with inheritance -go through or read on inheritance first

print("\n")


class Female(Person):
    def category(self):
        print("Female")


class Male(Person):
    def category(self):
        print("Male")

    def onlyMen(self):
        print("MEN")


male_obj = Male()
female_obj = Female()

male_obj.onlyMen()
male_obj.category()
female_obj.category()
