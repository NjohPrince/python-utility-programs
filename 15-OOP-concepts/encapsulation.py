# Encapsulation

# Encapsulation is the packing of data and functions that work on that data
# within a single object. By doing so, you can hide the internal state of
# the object from the outside. This is known as information hiding.

# A class is an example of encapsulation.
# A class bundles data and methods into a single unit.
# And a class provides the access to its attributes via methods.

# The idea of information hiding is that if you have an attribute that isn’t
# visible to the outside, you can control the access to its value to make
# sure your object is always has a valid state.

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
