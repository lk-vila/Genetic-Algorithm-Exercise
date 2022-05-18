import math
from typing import List
from . import AbstractFunction

class Ackley(AbstractFunction.AbstractFunction):
    def calculate(self, variables: List[float]) -> float:
        x = variables.pop(0)

        n: int = 2
        a: int = 20; b: float = 0.2; c: float = 2 * math.pi
        s1: int = 0; s2: int = 0

        for i in range(1, n):
            s1 = s1 + pow(x, 2)
            s2 = s2 + math.cos((c * x))

        z: float = -a * math.exp( -b * math.sqrt(1/n*s1)) - math.exp(1/n*s2) + a + math.exp(1)
        return z

    def interpretGene(self, gene: List[int]) -> List[float]:
        variables: List = []
        x = super().convertBinList(gene[0:20]) * 0.0001 - 40
        variables.append(x)
        return variables

    def getGeneLength(self):
        return 20
