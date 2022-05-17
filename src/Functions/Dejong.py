from queue import Queue
from . import AbstractFunction

class Dejong(AbstractFunction.AbstractFunction):
    def calculate(variables: Queue[float]) -> float:
        x = variables.get()
        y = variables.get()

        z: float = 100 * pow( (pow(x,2) - pow(y,2)), 2) + pow( (1 - pow(x, 2) ), 2)
        return z
