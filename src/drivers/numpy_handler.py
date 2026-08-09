import numpy as np

class NumpyHandler:
    def __init__(self) -> None:
        self.__np = np

    def standard_derivation(self, numbers):
        return self.__np.std(numbers)