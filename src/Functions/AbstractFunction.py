from queue import Queue
from typing import List


class AbstractFunction:
    def __init__(self) -> None:
        pass

    def calculate(variables: Queue[float]) -> float:
        pass

    def interpretGene(gene: List[int]) -> Queue[float]:
        pass

    def getGeneLength() -> int:
        pass

    def getName() -> str:
        pass
