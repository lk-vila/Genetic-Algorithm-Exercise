from Functions.AbstractFunction import Function


import AbstractFunction

class SumS(AbstractFunction):
    def calculate(x: float) -> float:
        n = 2
        s = 0

        for j in range(1, n):
            s = s + j * pow(x, 2)
        return s
