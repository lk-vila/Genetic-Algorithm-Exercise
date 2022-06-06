from typing import List

from Phenotype import Phenotype


class AbstractFunction:
    def __init__(self) -> None:
        pass

    def calculate(variables: List[float], phenotype: Phenotype) -> float:
        pass

    def interpretGene(gene: List[int]) -> List[float]:
        pass

    def getGeneLength() -> int:
        pass

    def getName(self) -> str:
        pass

    def convertBinList(self, list: List[int]) -> int:
        return int("".join(str(x) for x in list), 2)

    def binaryConversion(self, gene: List[int], min: int, max: int) -> List[float]:
        numLength = int(len(gene)/2)

        variables: List = []
        x = self.convertBinList(gene[0:numLength])
        y = self.convertBinList(gene[numLength:numLength * 2])
        
        x = min + (max - min) * x / (pow(2, numLength) - 1)
        y = min + (max - min) * y / (pow(2, numLength) - 1)

        variables.append(x)
        variables.append(y)

        return variables
