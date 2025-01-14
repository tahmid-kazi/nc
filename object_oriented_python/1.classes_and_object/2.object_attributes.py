class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy

whiskers = Pet("Whiskers", "cat", 6, 8)

# done (1/14/25)(1051-1103am)(Tue)

# TODO: Print Whiskers' initial attributes
print(f"Initial Attributes: {whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")

# TODO: Modify Whiskers' attributes:
#  - Decrease hunger by 3
#  - Increase energy by 2

whiskers.hunger = whiskers.hunger-3
whiskers.energy = whiskers.energy+2

# TODO: Print Whiskers' modified attributes
print(f"Modified Attributes: {whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")
