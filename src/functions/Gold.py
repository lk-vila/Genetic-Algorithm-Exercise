import math
from typing import List

from Phenotype import Phenotype
from . import AbstractFunction

class Gold(AbstractFunction.AbstractFunction):
    def calculate(self, variables: List[float], phenotype: Phenotype) -> None:
        x = variables.pop(0)
        y = variables.pop(0)

        a: float=1 + (x+y+1)**2 * ( 19 - 14*x + 3*x**2 - 14*y+6*x*y + 3*y**2 )
        b:float = 30 + (2*x-3*y)**2 * (18 - 32*x+12*x**2 + 48*y - 36*x*y + 27*y**2)
        phenotype.fitness = a*b
        return a*b


    def interpretGene(self, gene: List[int]) -> List[float]:
        min = -2
        max = 2
        return super().binaryConversion(gene,min,max)