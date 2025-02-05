import math

class AreaCalc:

    # 2/4/25)(Tue)(942-946pm) unit 5 done!!

    def calculate(self, length: int, width: int = None) -> float:
        if width == None:
            return round(math.pi * length**2, 2)
        else:
            return length * width
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
