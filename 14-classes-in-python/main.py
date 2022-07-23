#!/usr/bin/env python

"""main.py: working with classes in python"""

__author__ = "Njoh Noh Prince Junior"
__copyright__ = "Copyright 2022"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Njoh Noh Prince Junior"
__email__ = "jufredprince@gmail.com"

# program starts here - igonore what is above

# A class is a user-defined blueprint or prototype from which objects are created.

# class Person


class Person:
    def __init__(self, _name, _age, _code):
        self.name = _name  # name property
        self.age = _age  # age property
        self.__secret_code = _code  # private property

    def sayHi(self):  # introductory function -class method
        print('Hello, my name is ' + self.name +
              ' and I am ' + str(self.age) + ' years old!')

    def getSecretCode(self):
        return 'My secret code is {}'.format(self.__secret_code)


p1 = Person('Njoh Noh Prince Junior', 25, 123)  # object -instance of a class
p1.sayHi()

# accessing the name attribute
print("Person one has name {}".format(p1.name))

# trying to access a private variable
# print("Person one has secret code {}".format(p1.__secret_code))  # error

# this will work -leave previous line commented or do try and except 😊
print("Person one says: " + p1.getSecretCode())
