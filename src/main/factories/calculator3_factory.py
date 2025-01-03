"""Learnig about the Factory"""
from src.calculators.calculator_3 import Calculator3

from src.drivers.numpy_handler import NumpyHandler

def calculator3_factory():
    """Factory the calculator 3"""
    numpy_handler = NumpyHandler()
    calc = Calculator3(numpy_handler)
    return calc
