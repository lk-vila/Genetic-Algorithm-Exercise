import argparse
from concurrent.futures import thread
from queue import Queue
from random import Random
import sys
from Functions.AbstractFunction import AbstractFunction
from Functions.Ackley import Ackley
from Functions.Bump import Bump
from Functions.Dejong import Dejong
from Functions.Gold import Gold
from Functions.Rastringin import Rastringin
from Functions.SumS import SumS
from Population import Population

def main():
    checkpoint = args.checkpoint
    functionName: str = args.function
    numberOfGenerations: int = args.generations
    mutationProbability: float = args.mutation_probability
    populationSize: int = args.population_size
    seed: int = args.seed
    verbose: bool = args.verbose

    random : Random
    if seed:
        random = Random(seed)
    else:
        seed = Random().randrange(sys.maxsize)
        random = Random(seed)
        print(f"Seed: {seed}")


    function: AbstractFunction = globals()[functionName]()

    population: Population = Population(random, populationSize, function.getGeneLength(), mutationProbability)

    for i in range(1, numberOfGenerations+1):
        doIteration(function, population)

def doIteration(function: AbstractFunction, population: Population):
    for i, phenotype in enumerate(population.phenotypes):
        variables: Queue[float] = function.interpretGene(phenotype)
        phenotype.fitness = thread.start_new_thread(function.calculate(), ())


parser = argparse.ArgumentParser(description="Genetic algorithm optimization")
parser.add_argument("-c", "--checkpoint", type=str, help="path to checkpoint file")
parser.add_argument("-f", "--function", type=str, required=True, help="function to calculate fitness with")
parser.add_argument("-g", "--generations", type=int, required=True, help="number of generations to run")
parser.add_argument("-m", "--mutation-probability", type=float, required=True, help="probability that a given allele of a phenotype mutates")
parser.add_argument("-p", "--population-size", type=int, required=True, help="population size at the end of each generation")
parser.add_argument("-s", "--seed", type=int, help="seed for the pseudorandom generator to use")
parser.add_argument("-v", "--verbose", help="turn on verbosity", default=False, action="store_true")
args = parser.parse_args()

main()
