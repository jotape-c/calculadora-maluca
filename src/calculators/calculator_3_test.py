"""Test for calculator3"""

from pytest import raises
from src.drivers.numpy_handler import NumpyHandler
from .calculator_mock_request import MockRequest

from .calculator_3 import Calculator3


def test_calculate_with_variance_error():
    """testando calculate"""
    mock_request = MockRequest({"numbers": [1, 2, 3, -7, -18]})
    calculator3 = Calculator3(NumpyHandler())

    with raises(Exception) as execinfo:
        response = calculator3.calculate(mock_request)
    assert str(execinfo.value) == "Falha no processo: variancia menor que multiplicacao"


def test_calculate_with_bad_format_error():
    """testando calculate"""
    mock_request = MockRequest({"number": [1, 2, 3, -7, -18]})
    calculator3 = Calculator3(NumpyHandler())

    with raises(Exception) as execinfo:
        response = calculator3.calculate(mock_request)

    assert str(execinfo.value) == "body mal formatado"

def test_calculate():
    """testando calculate"""
    mock_request = MockRequest({"numbers": [1, 1, 1, 1, 100]})
    calculator3 = Calculator3(NumpyHandler())

    response = calculator3.calculate(mock_request)
    assert response ==  {'data': {'Calculator': 3, 'Variance': 1568.16, 'Success': True}}

