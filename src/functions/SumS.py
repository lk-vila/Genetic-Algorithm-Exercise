import math
from typing import List

from Phenotype import Phenotype
from . import AbstractFunction

class SumS(AbstractFunction.AbstractFunction):
    def calculate(self, variables: List[float], phenotype: Phenotype) -> None:
        x = variables.pop(0)
        y = variables.pop(0)

        s: float = 0

        s = s + 1 * pow(x, 2)

        s = s + 2 * pow(y, 2)

        z = s
        phenotype.fitness = -z


    def interpretGene(self, gene: List[int]) -> List[float]:
        variables: List = []
        x = super().convertBinList(gene[0:18]) * 0.0001 - 10
        y = super().convertBinList(gene[18:36]) * 0.0001 - 10
        variables.append(x)
        variables.append(y)
        return variables


    def getGeneLength(self):
        return 36
