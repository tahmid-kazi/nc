class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5

    # (1/14/25)(Tue)(1030-1033pm)
    def feed(self):
        # TODO: Implement this method
        # It should decrease the pet's hunger by 1
        # and print a message about feeding the pet
        self.hunger -= 1
        print(f"{self.name} has been fed.")
        print(f"{self.name}'s hunger level: {self.hunger}")

# Create a pet
my_pet = Pet("Fluffy")

# TODO: Feed the pet three times
my_pet.feed()
my_pet.feed()
my_pet.feed()

