import math
from typing import List
from . import AbstractFunction

class Rastringin(AbstractFunction.AbstractFunction):
    def calculate(x: float, y: float) -> float:
        z: float = pow(x, 2) + math.pow(y,2) - 10 * math.cos( 2 * math.pi * x) - 10 * math.cos(2 * math.pi * y) + 10
        return (z * -1)

    def getGeneLength(self):
        return 13

    def interpretGene(self, gene: List[int]) -> List[float]:
        variables: List = []
        x = super().convertBinList(gene[0:17]) * 0.0001 - 5
        y = super().convertBinList(gene[17:34]) * 0.0001 - 5
        variables.put(x)
        variables.put(y)
        return variables

    def getGeneLength(self):
        return 34
