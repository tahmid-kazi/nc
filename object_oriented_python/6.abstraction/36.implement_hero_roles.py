from abc import ABC, abstractmethod

# (2/5/25)(1235-1239am)(Tue night) (whole course finished!!!!!)

# TODO: Create the Attacker, Defender, and Healer interfaces
class Attacker:

    @abstractmethod
    def attack(self) -> None:
        pass


class Defender:
    
    @abstractmethod
    def defend(self) -> None:
        pass

class Healer:

    @abstractmethod
    def heal(self) -> None:
        pass



# Don't modify the following code
class Knight(Attacker, Defender, Healer):
    def __init__(self, name: str) -> None:
        self.name = name
    
    def attack(self) -> None:
        print(f"{self.name} attacks with sword!")
        
    def defend(self) -> None:
        print(f"{self.name} raises shield!")
        
    def heal(self) -> None:
        print(f"{self.name} uses healing potion!")

hero = Knight("Sir Galahad")
hero.attack()  
hero.defend()  
hero.heal()
