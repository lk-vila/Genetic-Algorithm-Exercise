
from asyncio.log import logger
from pickletools import genops
from random import Random

from utils.logger import Logger

LOG_TAG = "Phenotype"
COLOR = "yellow"

class Phenotype:
    def __init__(self, random: Random, mutationProbability: float, verbose: bool, length: int = None, genotype: list[int] = None) -> None:
        self.random = random
        self.verbose = verbose
        self.logger: Logger = Logger(verbose, LOG_TAG, COLOR)
        self.mutationProbability = mutationProbability

        if genotype != None:
            self.genotype = genotype
        else:
            self.genotype = self.generateRandomGenotype(length)


    def generateRandomGenotype(self, length: int):
        initialGenotype: list[int] = []

        # self.logger.log("Generating random genotype")
        for i in range(0,length):
            initialGenotype.append(self.random.randint(0, 1))
        # self.logger.log(initialGenotype.__str__())
        return initialGenotype


    def mutate(self):
        for allele, value in enumerate(self.genotype):
            num = self.random.random()
            if num < self.mutationProbability:
                self.flip(allele, value)


    def flip(self, allele, value):
        self.genotype[allele] = 1 if value == 0 else 0


    @property
    def genotype(self) -> list[int]:
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
