import math
from typing import List

from Phenotype import Phenotype
from . import AbstractFunction

class Rastringin(AbstractFunction.AbstractFunction):
    def calculate(self, variables: List[float], phenotype: Phenotype) -> None:
        A = 10
        y: float = [x**2 - A * math.cos(2 * math.pi * x) for x in variables]
        z = A*2 + sum(y)
        # function y=Rastrigin(x)

        # y=x(1)^2+x(2)^2-10*cos(2*pi*x(1))-10*cos(2*pi*x(2))+10;
        # y=-y;

        phenotype.fitness = z
        return -z

    def interpretGene(self, gene: List[int]) -> List[float]:
        min = -5
        max = 5
        return super().binaryConversion(gene,min,max)
