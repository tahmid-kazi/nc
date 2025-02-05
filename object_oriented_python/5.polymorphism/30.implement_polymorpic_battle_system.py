class Hero:
    def __init__(self, name: str, power: int):
        self.name = name
        self.health = 100
        self.power = power
    
    def attack(self) -> int:
        return self.power

# 2/4/25)(934-942pm)(Tue) done

# TODO: Implement the Warrior and Mage classes
class Warrior(Hero):
    def __init__(self, name: str, power: int):
        super().__init__(name, power) # ------------- NEEDED HELP

    def attack(self) -> int: return self.power+10


class Mage(Hero):
    def __init__(self, name: str, power: int):
        super().__init__(name, power) # ------------- NEEDED HELP
        health = 80

    def attack(self) -> int:
        return self.power+20


# TODO: Implement the battle function
def show_attack(hero: Hero) -> None:
    print(f"{hero.name} attacks with {hero.attack()} damage!")


# Do not modify the following code
warrior = Warrior("Bob", 20)
mage = Mage("Alice", 15)

show_attack(warrior)  
show_attack(mage)    
