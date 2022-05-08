import math
from Functions.AbstractFunction import Function

import AbstractFunction

class Rastrigin(AbstractFunction):
    def calculate(x: float, y: float) -> float:
        z: float = pow(x, 2) + math.pow(y,2) - 10 * math.cos( 2 * math.pi * x) - 10 * math.cos(2 * math.pi * y) + 10
        return (z * -1)
