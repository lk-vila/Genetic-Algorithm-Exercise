from Functions.AbstractFunction import Function


import AbstractFunction

class Gold(AbstractFunction):
    def calculate(x: float, y: float) -> float:
        a = 1 + pow((x + y + 1), 2) * pow( (19 - 14 * x + 3 * pow(x, 2) - 14 * y + 6 * x * y + 3 * pow(y, 2) ) ,2)
        b = 30 + pow((2 * x - 3 * y), 2) * (18 - 32 * x + 12 * pow(x, 2) + 48 * y - 36 * x * y + 27 * pow(y, 2) )
        return a*b
