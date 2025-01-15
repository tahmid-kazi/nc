class SuperHero:
    """
    A class to represent a superhero.

    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """
    #(1/14/25)(Tue)(1053-1057pm)
    def __init__(self, name: str, power: str, health: int):
        # TODO: Initialize the superhero's attributes here
        self.name = name
        self.power = power
        self.health = health


# TODO: Create Superhero instances
supe1 = SuperHero("Batman", "Intelligence", 100)
supe2 = SuperHero("Superman", "Strength", 150)

# TODO: Print out the attributes of each superhero
print(f"{supe1.name}\n{supe1.power}\n{supe1.health}")
print(f"{supe2.name}\n{supe2.power}\n{supe2.health}")
