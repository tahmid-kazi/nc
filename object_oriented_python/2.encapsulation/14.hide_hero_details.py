class SuperHero:
    # 1/31/25) Fri) 732/908-925pm)
    def __init__(self, name: str, health: int, power_level: int):
        self.name = name
        # TODO: Add the private attributes
        self.__health = health
        self.__power_level = power_level

    # TODO: Add the getter and setter methods
    
    # Getters
    #@property
    def get_health(self):
        return self.__health
    
    #@property
    def get_power_level(self):
        return self.__power_level

    # Setters
    #@health.setter
    def set_health(self, health: int):
        if health > 100:
            print("You can't set the health to more than 100")
        if health < 0:
            print("You can't set the health to less than 0")
        self.__health = health

    #@power_level.setter
    def set_power_level(self, power_level: int):
        if power_level > 10:
            print("You can't set the power level to more than 10")
        if  power_level < 1:
            print("You can't set the power level to less than 1")
        self.__power_level = power_level

super_hero = SuperHero("Batman", 80, 9)

print(super_hero.get_health()) # this should print 80
super_hero.set_health(110) # this should print You can't set the health to more than 100
super_hero.set_health(-10) # this should print You can't set the health to more than 100
super_hero.set_health(70) # this should print You can't set the health to more than 100

print(super_hero.get_power_level()) # this should print 9
super_hero.set_power_level(11) # this should print You can't set the power level to more than 10
super_hero.set_power_level(0) # this should print You can't set the power level to less than 1
super_hero.set_power_level(7) # this should print You can't set the power level to less than 1



# TODO: print the hero's attributes
print(f"Batman has {super_hero.get_health()} health and {super_hero.get_power_level()} power level") # this should print 9

