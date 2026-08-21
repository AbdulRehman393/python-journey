# Polymorphism = Greek word that means to have many forms or faces
#                Poly = Many
#                Morphe = Form
#                It means the ability of an object to have more than one form

#                TWO WAYS TO ACHIEVE POLYMORPHISM
#                1. Inheritance = An object can be treated as an instance of its parent class
#                2. "Duck Typing" = Object must have necessary attributes/methods

# the below example is focused on Inheritance

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass




class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Square(Shape):
    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width * self.width

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height / 2

class Pizza(Circle):
    def __init__(self,topping, radius):
        super().__init__(radius)
        self.topping = topping



shapes = [Circle(15), Square(10), Triangle(5, 6), Pizza("pepperoni", 15)]
# Our Pizza is considered a Pizza, it inherits from a Circle class so it's considered a Circle and our Circle class inherits from the Shape class
# Our Pizza has three forms,Our Pizza is considered a Pizza, it also considered a Circle, and it's also considered a Shape, it would make sense
# for it into a list of shapes because Pizza is also a Shape.

for shape in shapes:
    print(f"{shape.area()}cm^2")


