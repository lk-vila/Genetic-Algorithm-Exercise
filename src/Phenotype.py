from ast import List
from random import Random


class Phenotype:
    def __init__(self, random: Random, length: int, mutationProbability: float) -> None:
        self.random = random
        self.genotype = self.generateRandomGenotype(length)
        self.mutationProbability = mutationProbability


    def generateRandomGenotype(self, length: int):
        initialGenotype = [int]

        for i in range(0,length):
            initialGenotype.append(self.random.randint(0, 1))

        return initialGenotype


    def mutate(self):
        for allele, value in self.genotype:
            num = self.random.random()
            if num < self.mutationProbability:
                self.flip(allele, value)


    def flip(self, allele, value):
        self.genotype[allele] = 1 if value == 0 else 0


    @property
    def genotype(self):
        return self._genotype


    @genotype.setter
    def genotype(self, g):
        self._genotype = g


    @property
    def fitness(self):
        return self._fitness


    @fitness.setter
    def fitness(self, f: float):
        self._fitness = f
