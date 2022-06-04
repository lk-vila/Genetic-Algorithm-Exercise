from random import Random
from webbrowser import get
from xmlrpc.client import boolean

from Phenotype import Phenotype

from utils.logger import Logger

LOG_TAG = "Population"
COLOR = "purple"
class Population:


    def __init__(self, random: Random, verbose: boolean, populationSize: int, geneLength: int, mutationProbability: float) -> None:
        self.random = random
        self.logger = Logger(verbose, LOG_TAG, COLOR)
        self.phenotypes = [Phenotype]


        for i in range(0, populationSize):
            self.phenotypes.append(Phenotype(self.random, geneLength, mutationProbability))

    def mutate(self):
        self.logger.log("Starting mutation proccess")
        for phenotype in self.phenotypes:
            phenotype.mutate()
        self.logger.log("Done!")


    def breed(self):
        self.logger.log("Starting breeding proccess")

        for x in iter(self.phenotypes):
            breed


    def roulette(self) -> Phenotype:
        populationTemp = self.phenotypes.sort(key=lambda phenotype: phenotype.fitness, reverse=True)
        accumulatedFitness = []
        accumulatedFitness[0] = populationTemp[0].fitness
        for i in range(1, len(populationTemp)):
            accumulatedFitness[i] = accumulatedFitness[i-1] + populationTemp[i].fitness
        randomNum = self.random.randrange(0, accumulatedFitness[len(accumulatedFitness)])
        for j in range(0, len(accumulatedFitness)):
            if(randomNum < accumulatedFitness[j]):
                self.phenotypes= populationTemp[j]
        raise Exception("Could not retrieve phenotype from roulette")

    def tourney(self, populationSize: int):
        tempPopulation = self.phenotypes
        populationPicked = [Phenotype]

        randomNum = self.random.randrange(0, len(tempPopulation))
        populationPicked.insert(tempPopulation[randomNum])
        tempPopulation.pop(randomNum)
        tempPopulation.sort(key=lambda phenotype: phenotype.fitness, reverse=True)
        for i in range(1, len(self.phe)):
            populationPicked.insert(tempPopulation[0])
            tempPopulation.pop(0)
        self.phenotypes = populationPicked
