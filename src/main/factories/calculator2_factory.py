"""Learnig about the Factory"""
from src.calculators.calculator_2 import Calculator2

from src.drivers.numpy_handler import NumpyHandler

def calculator2_factory():
    """Factory the calculator 2"""
    numpy_handler = NumpyHandler()
    calc = Calculator2(numpy_handler)
    return calc
