class SuperHero:
    """
    A class to represent a superhero.
    
    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """
    # (1/14/25)(Tue)(1057-1104pm)
    def __init__(self, name: str, power: str, health: int):
        self.name = name
        self.power = power
        self.health = health
    
    # TODO: Define attack method and implement it
    def attack(self):
        print(f"{self.name} attacks with {self.power}!")

    # TODO: Define heal method and implment it
    def heal(self, add_health):
        self.health += add_health
        print(f"{self.name} heals {add_health} points. New health: {self.health}.")

# TODO: Create superhero instance
supe3 = SuperHero("Catwoman", "Agility", 120)

# TODO: Use the attack() and heal() method
supe3.attack()
supe3.heal(10)