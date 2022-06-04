import math
from typing import List

from Phenotype import Phenotype
from . import AbstractFunction

class SumS(AbstractFunction.AbstractFunction):
    def calculate(self, variables: List[float], phenotype: Phenotype) -> None:
        x = variables.pop(0)
        n: int = 2
        y: float = 0

        for j in range(1, n):
            y = y + j * pow(x, 2)

        phenotype.fitness = y


    def interpretGene(self, gene: List[int]) -> List[float]:
        variables: List = []
        x = super().convertBinList(gene[0:18]) * 0.0001 - 10
        variables.append(x)
        return variables


    def getGeneLength(self):
        return 18
