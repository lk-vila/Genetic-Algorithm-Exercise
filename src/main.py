import argparse
from ast import List
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


LOG_TAG = "Population"
COLOR = "green"
logger = None

def main():
    args = getArgs()

    checkpoint = args.checkpoint
    functionName: str = args.function
    numberOfGenerations: int = args.generations
    mutationProbability: float = args.mutation_probability
    populationSize: int = args.population_size
    seed: int = args.seed
    verbose: bool = args.verbose

    logger = Logger(verbose, LOG_TAG, COLOR)

    random : Random
    if seed:
        random = Random(seed)
    else:
        seed = Random().randrange(sys.maxsize)
        random = Random(seed)

    logger.log(f"Seed: {seed}")
    print("aaa")

    function: AbstractFunction = globals()[functionName]()

    population: Population = Population(random, verbose, populationSize, function.getGeneLength(), mutationProbability)

    for i in range(1, numberOfGenerations+1):
        doIteration(function, population)

def doIteration(function: AbstractFunction, population: Population):
    for i, phenotype in enumerate(population.phenotypes):
        variables: List[float] = function.interpretGene(phenotype)
        thread = threading.Thread(target=function.calculate, args=(variables, phenotype))
        thread.start()

main()
