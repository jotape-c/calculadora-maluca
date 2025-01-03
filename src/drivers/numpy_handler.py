"""Numpy padronizando o acesso a bibliotecas externas"""
from typing import List
import numpy


from .interfaces.driver_handler_interface import DriverHandleInterface

class NumpyHandler(DriverHandleInterface):
    """Disponibilizar o numpy a projeto todo"""
    def __init__(self) -> None:
        self.__np = numpy

    def standard_derivation(self, numbers: List[float]) -> float:
        """devio padrao"""
        return self.__np.std(numbers)

    def variance(self, numbers: List[float]) -> float:
        """variancia"""
        return self.__np.var(numbers)