from abc import ABC, abstractmethod

# (2/5/25)(1230-1235am)(Tue night)

# TODO: Implement Superpower class
class Superpower:
    def __init__(self, name: str, power_level: int):
        self.name = name
        self.power_level = power_level
        self.is_active = False
    
    def get_power_level(self) -> int:
        return self.power_level

    @abstractmethod
    def activate(self) -> None:
        pass

    @abstractmethod
    def deactivate(self) -> None:
        pass


# Don't modify the following code
class LaserBeam(Superpower):
    def activate(self) -> None:
        self.is_active = True
        print(f"{self.name} activated!")
        
    def deactivate(self) -> None:
        self.is_active = False
        print(f"{self.name} deactivated!")

class SuperStrength(Superpower):
    def activate(self) -> None:
        self.is_active = True
        print(f"{self.name} activated!")
        
    def deactivate(self) -> None:
        self.is_active = False
        print(f"{self.name} deactivated!")

laser_beam = LaserBeam("Laser Beam", 10)
super_strength = SuperStrength("Super Strength", 8)

print(laser_beam.get_power_level())
print(super_strength.get_power_level())

laser_beam.activate()
super_strength.activate()

laser_beam.deactivate()
super_strength.deactivate()
