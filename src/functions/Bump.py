import math
from typing import List

from Phenotype import Phenotype
from . import AbstractFunction

class Bump(AbstractFunction.AbstractFunction):
    def calculate(self, variables: List[float], phenotype: Phenotype) -> None:
        x = variables.pop(0)
        y = variables.pop(0)

        z: float
        if((x * y) < 0.75):
            z = None
        elif((x+y) > 7.5 * 2):
            z = None
        else:
            temp0 = pow(math.cos(x), 4) + pow(math.cos(y), 4)
            temp1 = 2 * (pow(math.cos(x), 2)) * (pow(math.cos(y), 2))
            temp2 = math.sqrt(pow(x, 2) + 2 * pow(y, 2))
            z = -abs( (temp0 - temp1) / temp2)

        phenotype.fitness = 1/z


    def interpretGene(self, gene: List[int]) -> List[float]:
        min = 0
        max = 10
        return super.binaryConversion(gene,min,max)


    def getGeneLength(self):
        return 34
