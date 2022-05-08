from Functions.AbstractFunction import Function


import AbstractFunction

class SumS(AbstractFunction):
    def calculate(x: float) -> float:
        n: int = 2
        s: float = 0

        for j in range(1, n):
            s = s + j * pow(x, 2)
        return s
