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

    def roulette(phenotypes, random: Random) -> Phenotype:
        populationTemp = phenotypes.sort(key=lambda phenotype: phenotype.fitness, reverse=True)
        accumulatedFitness = []
        accumulatedFitness[0] = populationTemp[0].fitness
        for i in range(1, len(populationTemp)):
            accumulatedFitness[i] = accumulatedFitness[i-1] + populationTemp[i].fitness
        randomNum = random.randrange(0, accumulatedFitness[len(accumulatedFitness)])
        for j in range(0, len(accumulatedFitness)):
            if(randomNum < accumulatedFitness[j]):
                return populationTemp[j]
        raise Exception("Could not retrieve phenotype from roulette")

    def tourney(phenotypes, random: Random, populationSize: int):
        tempPopulation = phenotypes
        populationPicked = [Phenotype]

        randomNum = random.randrange(0, len(tempPopulation))
        populationPicked.insert(tempPopulation[randomNum])
        tempPopulation.pop(randomNum)
        tempPopulation.sort(key=lambda phenotype: phenotype.fitness, reverse=True)
        for i in range(1, populationSize):
            populationPicked.insert(tempPopulation[0])
            tempPopulation.pop(0)
        return populationPicked
