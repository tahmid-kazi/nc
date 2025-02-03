class SuperHero:
    def __init__(self, name: str, power: str):
        self.name = name
        self.power = power
    
    def attack(self) -> None:
        print(f"{self.name} is attacking with {self.power}")

# TODO: Create a Avenger class that inherits from the SuperHero class
# TODO: Override the __init__ method to add a team property to the Avenger class
# TODO: Call the attack method of the SuperHero class from the Avenger class

# 2/2/25) Sun) 950-955pm) done

class Avenger(SuperHero):
    def __init__(self, name: str, power: str, team: str):
        #extend the parent, not replace it
        super().__init__(name, power)  # holy shit I got this correct
        self.team = team

    def attack(self) -> None:
        super().attack() # holy shit I got this correct


# Don't change the code below
avenger = Avenger("Iron Man", "repulsor beams", "Avengers")
print(avenger.name)
print(avenger.power)
print(avenger.team)
avenger.attack()
