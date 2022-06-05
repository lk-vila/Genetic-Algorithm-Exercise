import math
from typing import List

from Phenotype import Phenotype
from . import AbstractFunction

class Ackley(AbstractFunction.AbstractFunction):

    def calculate(self, variables: List[float], phenotype: Phenotype) -> None:
        x = variables.pop(0)
        y = variables.pop(0)

        n: int = 2
        a: int = 20; b: float = 0.2; c: float = 2 * math.pi
        s1: int = 0; s2: int = 0

    
        s1 = s1 + pow(x, 2)
        s2 = s2 + math.cos((c * x))

        s1 = s1 + pow(y, 2)
        s2 = s2 + math.cos((c * y))

        z: float = -a * math.exp( -b * math.sqrt(1/n*s1)) - math.exp(1/n*s2) + a + math.exp(1)
        phenotype.fitness = -z


    def interpretGene(self, gene: List[int]) -> List[float]:
        min = -40
        max = 40
        return super.binaryConversion(gene,min,max)


    def getGeneLength(self):
        return 40
