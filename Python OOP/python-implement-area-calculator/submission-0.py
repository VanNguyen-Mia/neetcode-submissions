import math

class AreaCalc:
    # TODO: Implement calculate method
    def calculate(self, *args) -> float:
        if len(args) == 1:
            res = round(math.pi * (args[0]**2), 2)
        elif len(args) == 2:
            res = args[0] * args[1]
        return res
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
