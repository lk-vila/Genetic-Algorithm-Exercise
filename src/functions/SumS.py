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
        min = -10
        max = 10
        return super.binaryConversion(gene,min,max)



    def getGeneLength(self):
        return 36
