import argparse

def getArgs() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Genetic algorithm optimization")
    parser.add_argument("-c", "--checkpoint", type=str, help="path to checkpoint file")
    parser.add_argument("-f", "--function", type=str, required=True, help="function to calculate fitness with")
    parser.add_argument("-g", "--generations", type=int, required=True, help="number of generations to run")
    parser.add_argument("-m", "--mutation-probability", type=float, required=True, help="probability that a given allele of a phenotype mutates")
    parser.add_argument("-p", "--population-size", type=int, required=True, help="population size at the end of each generation")
    parser.add_argument("-r", "--resolution", type=int, required=True, help="length of the genotype array")
    parser.add_argument("-s", "--seed", type=int, help="seed for the pseudorandom generator to use")
    parser.add_argument("-v", "--verbose", help="turn on verbosity", default=False, action="store_true")
    return parser.parse_args()
