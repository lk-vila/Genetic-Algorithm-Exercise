from queue import Queue
import math
from . import AbstractFunction

class Ackley(AbstractFunction.AbstractFunction):
    def calculate(variables: Queue[float]) -> float:
        x = variables.get()

        n: int = 2
        a: int = 20; b: float = 0.2; c: float = 2 * math.pi
        s1: int = 0; s2: int = 0

        for i in range(1, n):
            s1 = s1 + pow(x, 2)
            s2 = s2 + math.cos((c * x))

        z: float = -a * math.exp( -b * math.sqrt(1/n*s1)) - math.exp(1/n*s2) + a + math.exp(1)
        return z
