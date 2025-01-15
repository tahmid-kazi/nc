class Pet:
    # TODO: Implement the __init__ method here
    # done (1/14/25)(Tue)(1035-1037pm)
    def __init__(self, name, species, age1):
        self.name = name
        self.species = species
        self.age = age1



# Don't modify the code below this line
fluffy = Pet("Fluffy", "cat", 3)
buddy = Pet("Buddy", "dog", 2)

print(f"{fluffy.name} is a {fluffy.age} year old {fluffy.species}.")
print(f"{buddy.name} is a {buddy.age} year old {buddy.species}.")
