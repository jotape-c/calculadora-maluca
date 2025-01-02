"""Tests for calculator_1.py"""
from typing import Dict
from pytest import raises

from .calculator_1 import Calculator1

class MockRequest:
    """Classe de mokada pra teste"""
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    """Something"""
    mock_request = MockRequest(body={'number': 1})

    calculator_1 = Calculator1()
    response = calculator_1.calculate(mock_request)
    print(response)

    # Formato da resposta
    assert 'data' in response
    assert 'Calculator' in response['data']
    assert 'Result' in response['data']

    # Assertividade da resposta
    assert response['data']['Result'] == 14.25
    assert response['data']['Calculator'] == 1

def test_calculate_with_body_error():
    """Validar se o request for mal formatado"""
    mock_request = MockRequest(body={'numbe': 1})
    calculator_1 = Calculator1()

    with raises(ValueError) as excinfo:
        calculator_1.calculate(mock_request)

    assert str(excinfo.value) == 'body mal formatado'
