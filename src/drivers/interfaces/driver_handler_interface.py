"""Content of driver_handler_interface.py"""
from abc import ABC, abstractmethod
from typing import List

class DriverHandleInterface(ABC):
    """Driver handle interface"""

    @abstractmethod
    def standard_derivation(self, numbers: List[float]) -> float:
        pass

    @abstractmethod
    def variance(self, numbers: List[float]) -> float:
        pass
