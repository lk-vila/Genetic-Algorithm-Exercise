from random import Random

from Phenotype import Phenotype


class Population:
    def __init__(self, random: Random, populationSize: int, geneLength: int) -> None:
        self.random = random
        self.phenotypes = [Phenotype]

        for i in range(0, populationSize):
            self.phenotypes.append(Phenotype(geneLength, self.random))

    def mutate(self, probability: float):
        for phenotype in self.phenotypes:
            phenotype.mutate(probability)
