from Functions.AbstractFunction import Function


import AbstractFunction

class Dejong(AbstractFunction):
    def calculate(x: float, y: float) -> float:
        z: float = 100 * pow( (pow(x,2) - pow(y,2)), 2) + pow( (1 - pow(x, 2) ), 2)
        return z
