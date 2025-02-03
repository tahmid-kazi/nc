class Animal:

    # 501-925pm) 4.5hrs gone)
    # 932-942pm) 2/2/25) Sun) this chapt done

    def __init__(self, name: str):
        self.name = name

    def make_sound(self) -> None:
        print("Animal makes a sound")

# TODO: Create a Dog class and a Cat class that inherit from the `Animal` class.
# TODO: Override the `make_sound` method in the `Dog` class to make the dog bark.
# TODO: Override the `make_sound` method in the `Cat` class to make the cat meow.

class Dog(Animal):
    def make_sound(self) -> None:
        print(f"{self.name} is barking")



class Cat(Animal):
    def make_sound(self)-> None:
        print(f"{self.name} is meowing")



# Do not modify the code below
animal = Animal("Cow")
animal.make_sound() # Output: Animal makes a sound
dog = Dog("Max")
dog.make_sound() # Output: Max is barking
cat = Cat("Luna")
cat.make_sound() # Output: Luna is meowing
