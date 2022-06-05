from asyncio.log import logger
from random import Random
from typing import List
from webbrowser import get
''

from Phenotype import Phenotype

from utils.logger import Logger

LOG_TAG = "Population"
COLOR = "purple"

class Population:

    def __init__(self, random: Random, verbose: bool, populationSize: int, geneLength: int, mutationProbability: float) -> None:
        self.random = random
        self.verbose = verbose
        self.logger = Logger(verbose, LOG_TAG, COLOR)
        self.phenotypes: list[Phenotype] = []
        self.populationSize = populationSize
        self.geneLength = geneLength
        self.mutationProbability = mutationProbability

        self.logger.log("Generating population")
        self.addRandom(populationSize)
        

    def addRandom(self, size: int) -> None:
        for i in range(0, size):
            phenotype: Phenotype = Phenotype(random=self.random, verbose=self.verbose, length=self.geneLength, mutationProbability=self.mutationProbability)
            self.phenotypes.append(phenotype)

    def mutate(self):
        self.logger.log("Starting mutation proccess")
        for phenotype in self.phenotypes:
            phenotype.mutate()
        self.logger.log("Done!")


    def crossover(self):
        self.logger.log("Starting crossover proccess")

        children: List[Phenotype] = []
        for i in range(0, int(self.populationSize/2)):
            dad = self.random.choice(self.phenotypes)
            mom = self.random.choice(self.phenotypes)
            children.append(self.breed(dad, mom))
        self.logger.log("Done!")
        self.phenotypes += children


    def breed(self, dad: Phenotype, mom: Phenotype) -> Phenotype:
        genotype: list[int] = []
        for i in range(self.geneLength):
            choice = self.random.randint(0, 1)
            if choice == 0:
                genotype.append(dad.genotype[i])
            else: 
                genotype.append(mom.genotype[i])
        child: Phenotype = Phenotype(random=self.random, verbose=self.verbose, genotype=genotype, mutationProbability=self.mutationProbability)
        return child


    def roulette(self) -> Phenotype:
        populationTemp = self.phenotypes.sort(key=lambda phenotype: phenotype.fitness, reverse=True)
        accumulatedFitness = []
        accumulatedFitness[0] = populationTemp[0].fitness
        for i in range(1, len(populationTemp)):
            accumulatedFitness[i] = accumulatedFitness[i-1] + populationTemp[i].fitness
        randomNum = self.random.randrange(0, accumulatedFitness[len(accumulatedFitness)])
        for j in range(0, len(accumulatedFitness)):
            if(randomNum < accumulatedFitness[j]):
                return populationTemp[j]
        raise Exception("Could not retrieve phenotype from roulette")


    def tourney(self):
        tempPopulation = self.phenotypes
        populationPicked = [Phenotype]

        randomNum = self.random.randrange(0, len(tempPopulation))
        populationPicked.insert(tempPopulation[randomNum])
        tempPopulation.pop(randomNum)
        tempPopulation.sort(key=lambda phenotype: phenotype.fitness, reverse=True)
        for i in range(1, len(self.phenotypes)):
            populationPicked.insert(tempPopulation[0])
            tempPopulation.pop(0)
        self.phenotypes = populationPicked


    def biClassSelection(self, pPercentage: float):
        upperClass = []
        lowerClass = []
        self.phenotypes.sort(key=lambda phenotype: phenotype.fitness, reverse=True)
        upperClass = self.phenotypes[0 : int(self.populationSize * pPercentage)]
        lowerClass = self.phenotypes[len(self.phenotypes) - int(self.populationSize * (1 - pPercentage)) : len(self.phenotypes)]
        self.phenotypes = upperClass + lowerClass
