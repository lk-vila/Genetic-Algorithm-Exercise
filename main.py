import argparse

def main():
    pass


parser = argparse.ArgumentParser(description="Genetic algorithm simulator")
parser.add_argument("-c", "--checkpoint", type=str, help="path to checkpoint file")
parser.add_argument("-f", "--fuction", type=str, help="function to calculate fitness with")
parser.add_argument("-g", "--generations", type=int, required=True, help="number of generations to run")
parser.add_argument("-p", "--population-size", type=int, required=True, help="population size at the end of each generation")
parser.add_argument("-s", "--seed", type=int, help="seed for the pseudorandom generator to use")
parser.add_argument("-v", "--verbose", help="turn on verbosity", action="store_true")
parser.parse_args()

main()
