# multiple inheritance = inherit from more than one parent class
#                        C(A,B)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                          A child can access what its parent inherited from its own parent (grandparent).
#                          C(B) <- B(A) <- A

class Animal:
    # We define the name attribute in the Animal class.
    # Child classes inherit this attribute through inheritance.
    def __init__(self,name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tonny")
fish = Fish("Nemo")

rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()

# Rabbit, Hawk, and Fish will inherit everything the Prey and Predator class have
rabbit.eat()
rabbit.sleep()
hawk.eat()
hawk.sleep()
fish.eat()
fish.sleep()
