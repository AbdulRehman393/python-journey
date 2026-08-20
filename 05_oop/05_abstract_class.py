# Abstract class: A class that cannot be instantiated on its own; meant to be subclassed (means The class is designed/intended to be used as a parent class,
#                 so other classes can inherit from it.)
#                 They can contain abstract methods, which are declared but have no implementation
#                 Abstract class benefits:
#                 1. Prevent instantiation of the class itself
#                 2. Require children to use inherited abstract methods

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod         # To declare an abstract method we need to use a decorator
    def go(self):           # Abstract methods are methods that subclasses are required to implement.
      pass                  # They can have no implementation (pass) or can even contain some implementation.


    @abstractmethod
    def stop(self):
        print("You stop the vehicle")


class Car(Vehicle):
    # If a class is inherited from a parent that's abstract and there is abstract methods, we have to finish defining those methods
    def go(self):
        print("You drive the car")

    def stop(self):
        print("You stop the car")
        #If you want to use the parent's implementation
        #super().stop()


class  Bike(Vehicle):

    def go(self):
        print("You ride the bike")

    def stop(self):
        print("You stop the bike")

class Boat(Vehicle):

    def go(self):
        print("You sail the boat")

    def stop(self):
        print("You anchor the boat")


car = Car()
car.go()
car.stop()

bike = Bike()
bike.go()
bike.stop()

boat = Boat()
boat.go()
boat.stop()