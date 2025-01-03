"""Test for calculator 2 file"""
from typing import List

from src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandleInterface

from .calculator_2 import Calculator2
from .calculator_mock_request import MockRequest

class MockDriverHandler(DriverHandleInterface):
    """s"""
    def standard_derivation(self, numbers: List[float]):
        return 3

# Integração entre NumpyHandler e Calculator2
def test_calculator_integration():
    """Testando"""
    mock_request = MockRequest({'numbers': [1.88,2,8.335,4.4,5.8]})
    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)
    response = calculator_2.calculate(mock_request)
    print(response)

    # Formatos de entradas
    assert isinstance(response, dict)
    assert response ==  {'data': {'Calculator': 2, 'Result': 0.04789715335932148}}

# Integração entre NumpyHandler e Calculator2
def test_calculator():
    """Testando"""
    mock_request = MockRequest({'numbers': [1.88,2,8.335,4.4,5.8]})
    driver = MockDriverHandler()
    calculator_2 = Calculator2(driver)
    response = calculator_2.calculate(mock_request)
    print(response)

    # Formatos de entradas
    assert isinstance(response, dict)
    assert response ==  {'data': {'Calculator': 2, 'Result': 0.04789715335932148}}
