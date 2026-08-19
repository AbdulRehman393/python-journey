# Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               class Child(Parent)   these are also known as class Sub(Super)

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Rat(Animal):
    pass             # You can use "pass" as a placeholder inside a child class. so pass means "Do nothing for here now."


dog = Dog("Lucy")
cat = Cat("Kitty")
rat = Rat("Petra")

print(dog.name)
print(cat.name)
print(rat.name)
dog.eat()
cat.sleep()
dog.speak()
cat.speak()



