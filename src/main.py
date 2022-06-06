from ast import List
from time import sleep
import matplotlib.pyplot as plt
import threading
from random import Random
import sys
from utils.parser import getArgs
from utils.logger import Logger
from functions.AbstractFunction import AbstractFunction
from functions.Ackley import Ackley
from functions.Bump import Bump
from functions.Dejong import Dejong
from functions.Gold import Gold
from functions.Rastringin import Rastringin
from functions.SumS import SumS
from Phenotype import Phenotype
from Population import Population


LOG_TAG = "Main"
COLOR = "green"

xpoints = []
fitnessMeanList = []
fitnessBestList = []

def main():
    args = getArgs()

    checkpoint = args.checkpoint
    functionName: str = args.function
    numberOfGenerations: int = args.generations
    mutationProbability: float = args.mutation_probability
    populationSize: int = args.population_size
    resolution: int = args.resolution
    seed: int = args.seed
    verbose: bool = args.verbose

    global logger
    logger = Logger(verbose, LOG_TAG, COLOR)

    random : Random
    if seed:
        random = Random(seed)
    else:
        seed = Random().randrange(sys.maxsize)
        random = Random(seed)

    logger.log(f"Seed: {seed}")

    function: AbstractFunction = globals()[functionName]()

    population: Population = Population(random, verbose, populationSize, resolution, mutationProbability)

    for i in range(1, numberOfGenerations+1):
        logger.log(f"Starting iteration {i}")
        xpoints.append(i)
        if i > 1:
            population.phenotypes.sort(key=lambda phenotype: phenotype.fitness, reverse=True)
        doIteration(function, population)

    variables: List[float] = function.interpretGene(population.phenotypes[0].genotype)
    logger.log(f"Best output: {function.calculate(variables, population.phenotypes[0])}")

    logger.log(f"Seed: {seed}")

    plt.plot(xpoints, fitnessBestList, label="Best Fitness")
    plt.plot(xpoints, fitnessMeanList, label="Population Fitness")
    plt.legend(loc="upper left")
    plt.title(f"{functionName}")
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.show()

def doIteration(function: AbstractFunction, population: Population):

    population.addRandom(int(population.populationSize*0.1))
    population.crossover()
    population.mutate()

    for i, phenotype in enumerate(population.phenotypes):
        variables: List[float] = function.interpretGene(phenotype.genotype)
        if i == 0:
            logger.log(f"Best variables | x: {variables[0]} y: {variables[1]} ")
        # thread = threading.Thread(target=function.calculate, args=(variables, phenotype))
        # thread.start()
        function.calculate(variables, phenotype)
    
    population.biClassSelection(1)
    # population.tourney()

    fitnessMean: float = 0
    for phenotype in population.phenotypes:
        fitnessMean += phenotype.fitness

    fitnessMean = fitnessMean/len(population.phenotypes)
    fitnessMeanList.append(fitnessMean)

    fitnessBest = population.phenotypes[0].fitness
    fitnessBestList.append(fitnessBest)


    logger.log(f"Fitness Best: {'{:e}'.format(fitnessBest)}")
    logger.log(f"Fitness Mean: {'{:e}'.format(fitnessMean)}")
    logger.log(f"Final population size: {len(population.phenotypes)}")
    

main()
