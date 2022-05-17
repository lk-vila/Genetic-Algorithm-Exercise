from random import Random

from Phenotype import Phenotype


class Population:
    def __init__(self, random: Random, populationSize: int, geneLength: int, mutationProbability: float) -> None:
        self.random = random
        self.phenotypes = [Phenotype]

        for i in range(0, populationSize):
            self.phenotypes.append(Phenotype(self.random, geneLength, mutationProbability))

    def mutate(self):
        for phenotype in self.phenotypes:
            phenotype.mutate()
