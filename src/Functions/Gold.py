from queue import Queue
from . import AbstractFunction

class Gold(AbstractFunction.AbstractFunction):
    def calculate(variables: Queue[float]) -> float:
        x = variables.get()
        y = variables.get()

        a: float = 1 + pow((x + y + 1), 2) * pow( (19 - 14 * x + 3 * pow(x, 2) - 14 * y + 6 * x * y + 3 * pow(y, 2) ) ,2)
        b: float = 30 + pow((2 * x - 3 * y), 2) * (18 - 32 * x + 12 * pow(x, 2) + 48 * y - 36 * x * y + 27 * pow(y, 2) )
        return a*b

    def getGeneLength(self):
        return 10
