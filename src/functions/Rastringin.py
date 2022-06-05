import math
from typing import List

from Phenotype import Phenotype
from . import AbstractFunction

class Rastringin(AbstractFunction.AbstractFunction):
    def calculate(self, variables: List[float], phenotype: Phenotype) -> None:
        x: float = variables.pop(0)
        y: float = variables.pop(0)
        z: float = pow(x, 2) + math.pow(y,2) - 10 * math.cos( 2 * math.pi * x) - 10 * math.cos(2 * math.pi * y) + 10
        phenotype.fitness = 1/(z * -1)


    def getGeneLength(self):
        return 13


    def interpretGene(self, gene: List[int]) -> List[float]:
        min = -5
        max = 5
        return super.binaryConversion(gene,min,max)


    def getGeneLength(self):
        return 34
