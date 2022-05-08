from ast import List
from random import Random


class Phenotype:
    def __init__(self, random: Random, length: int) -> None:
        self.random = random
        self.genotype = self.generateRandomGenotype(length)


    def generateRandomGenotype(self, length: int) -> List[int]:
        genotype = []

        for i in range(0,length):
            genotype.append(self.random.randint(0, 1))

        return genotype


    def mutate(self, probability: float):
        for allele, value in self.genotype:
            num = self.random.random()
            if num < probability:
                self.flip(allele, value)


    def flip(self, allele, value):
        self.genotype[allele] = 1 if value == 0 else 0


    @property
    def genotype(self):
        return self.genotype


    @genotype.setter
    def genotype(self, genotype):
        self.genotype = genotype


    @property
    def fitness(self):
        return self.fitness


    @fitness.setter
    def fitness(self, fitness: float):
        self.fitness = fitness
