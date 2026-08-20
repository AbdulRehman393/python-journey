# super() = Function used in a child class to call methods from a parent class (super class).
#           Allows you to extend the functionality of the inherited methods.

# Method Overriding =           When a child class provides its own implementation
#                               of a method that already exists in the parent class,
#                               the child's version is used when called on a child object.

class Shape:
    def __init__(self,color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self,color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        # If you would like to extend the functionality of a method from a parent, you can use the super function
        super().describe()
        print(f"It is a Circle with an area of {3.14 * self.radius * self.radius}cm^2")


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"It is a Square with an area of {self.width * self.width}cm^2")


class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"It is a Triangle with an area of {self.height * self.width / 2}cm^2")


# We can even use keyword arguments for better readability
shape = Shape(color="Red", is_filled=True)
print(shape.color)
print(shape.is_filled)
shape.describe()

print("--------------------")

circle = Circle(color="Yellow", is_filled=True,radius = 5)
print(circle.color)
print(circle.is_filled)
print(circle.radius)
circle.describe()

print("--------------------")

square = Square(color="Blue", is_filled=True, width = 3)
print(square.color)
print(square.is_filled)
print(square.width)
square.describe()

print("--------------------")

triangle = Triangle(color="Purple", is_filled=True, width = 3, height = 2)
print(triangle.color)
print(triangle.is_filled)
print(triangle.width)
print(triangle.height)
triangle.describe()



