from typing import List


class AbstractFunction:
    def __init__(self) -> None:
        pass

    def calculate(variables: List[float]) -> float:
        pass

    def interpretGene(gene: List[int]) -> List[float]:
        pass

    def getGeneLength() -> int:
        pass

    def getName(self) -> str:
        pass

    def convertBinList(self, list: List[int]) -> int:
        return int("".join(str(x) for x in list), 2)
