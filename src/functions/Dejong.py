import math
from typing import List

from Phenotype import Phenotype
from . import AbstractFunction

class Dejong(AbstractFunction.AbstractFunction):
    def calculate(self, variables: List[float], phenotype: Phenotype) -> float:
        x = variables.pop(0)
        y = variables.pop(0)

        z: float = 100 * pow( (pow(x,2) - pow(y,2)), 2) + pow( (1 - pow(x, 2) ), 2)
        phenotype.fitness = z


    def interpretGene(self, gene: List[int]) -> List[float]:
        min = -2
        max = 2
        return super.binaryConversion(gene,min,max)


    def getGeneLength(self):
        return 32
