from abc import ABC, abstractmethod

# 2/5/25)(1225-1228am)(Tue night)

# ------------------------------------------------------------
# Key Note:
# ------------------------------------------------------------

# Abstract classes can have both concrete and abstract methods
# Interfaces are pure-play abstract methods
# ------------------------------------------------------------


# TODO: Create a Superhero interface
class Superhero:
    @abstractmethod
    def fly(self) -> str:
        pass
    
    @abstractmethod
    def use_power(self) -> str:
        pass

class Superman(Superhero):
    def fly(self) -> str:
        return "Up, up and away!"
    
    def use_power(self) -> str:
        return "Using heat vision"

class WonderWoman(Superhero):
    def fly(self) -> str:
        return "Soaring through the clouds!"
    
    def use_power(self) -> str:
        return "Using lasso of truth"



# Don't modify the code below
superman = Superman()
wonder_woman = WonderWoman()

print(isinstance(superman, Superhero)) 
print(isinstance(wonder_woman, Superhero))
