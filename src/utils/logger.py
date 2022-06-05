from .time_service import get_time

fg = {
    "reset":'\033[0m',
    "black":'\033[30m',
    "red":'\033[31m',
    "green":'\033[32m',
    "orange":'\033[33m',
    "blue":'\033[34m',
    "purple":'\033[35m',
    "cyan":'\033[36m',
    "lightgrey":'\033[37m',
    "darkgrey":'\033[90m',
    "lightred":'\033[91m',
    "lightgreen":'\033[92m',
    "yellow":'\033[93m',
    "lightblue":'\033[94m',
    "pink":'\033[95m',
    "lightcyan":'\033[96m',
}

class Logger:

    def __init__(self, verbose, LOG_TAG, COLOR) -> None:
       self.verbose = verbose
       self.LOG_TAG = LOG_TAG
       self.COLOR = COLOR


    def log(self, string: str) -> str:
        if self.verbose:
            print(f"{fg[self.COLOR]}{get_time()}-{self.LOG_TAG}: {fg['reset']}" + string)
