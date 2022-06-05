import math
from typing import List

from Phenotype import Phenotype
from . import AbstractFunction

class Gold(AbstractFunction.AbstractFunction):
    def calculate(self, variables: List[float], phenotype: Phenotype) -> None:
        x = variables.pop(0)
        y = variables.pop(0)

        a: float = 1 + pow((x + y + 1), 2) * (19 - 14 * x + (3 * pow(x, 2))) - 14 * y + 6 * x * y + (3 * pow(y, 2) )
        b: float = 30 + pow((2 * x - 3 * y), 2) * (18 - 32 * x + 12 * pow(x, 2) + 48 * y - 36 * x * y + 27 * pow(y, 2) )
        phenotype.fitness = a*b


    def interpretGene(self, gene: List[int]) -> List[float]:
        variables: List = []
        x = super().convertBinList(gene[0:16]) * 0.0001 - 2
        y = super().convertBinList(gene[16:32]) * 0.0001 - 2
        if x > 2:
            x = 2
        if y > 2:
            y = 2

        variables.append(x)
        variables.append(y)

        return variables


    def getGeneLength(self):
        return 32
