class Animal:
    # no work done (2/3/25)(Mon)
    # (2/4/25)(915pm) finally started
    # this chapt done (919-924pm)(2/4/25)(Tue)

    def __init__(self, name: str):
        self.name = name
    
    def make_sound(self) -> None:
        print("Animal is making a sound")


# TODO: Create the Dog and Cat classes with make_sound method
class Dog(Animal):

    def make_sound(self) -> None:
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def make_sound(self) -> None:
        print(f"{self.name} says: Meow!")

# TODO: Create a common interface that takes any object of type Animal (or its subclasses) and calls their make_sound method
#--------------
# REVISIT THIS
#--------------
def make_sound(animal: Animal) -> None:
    animal.make_sound()

# Do not change the code below
animal = Animal("Rabbit")
animal.make_sound()

animal = Dog("Buddy")
animal.make_sound()

animal = Cat("Whiskers")
animal.make_sound()
