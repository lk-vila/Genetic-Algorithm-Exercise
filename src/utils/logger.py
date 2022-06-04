from termcolor import colored

from Population import COLOR
from .time_service import get_time


class Logger:

    def __init__(self, verbose, LOG_TAG, COLOR) -> None:
       self.verbose = verbose
       self.LOG_TAG = LOG_TAG
       self.COLOR = COLOR


    def log(self, string: str) -> str:
        if self.verbose:
            print(colored(f"{get_time()}{self.LOG_TAG}: ", COLOR) + string)
