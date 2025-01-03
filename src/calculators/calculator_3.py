"""Calcutator 3"""
from typing import Dict, List

from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandleInterface


class Calculator3:
    """ "Calculator 3"""

    def __init__(self, driver_hander: DriverHandleInterface) -> None:
        self.__driver_handler = driver_hander

    def __validate_body(self, body: Dict) -> List[float]:
        """Validar body"""
        if 'numbers' not in body:
            raise TypeError("body mal formatado")

        input_data = body["numbers"]
        return input_data

    def __calculate_variance(self, numbers: List[float]) -> float:
        """"""
        variance = self.__driver_handler.variance(numbers)
        return float(variance)

    def __calculate_multiplication(self, numbers: List[float]) -> float:
        """"""
        multiplication = 1
        for num in numbers:
            multiplication *= num
        return multiplication

    def __verify_results(self, variance: float, multiplication: float) -> None:
        """Verificar"""
        if variance < multiplication:
            raise Exception('Falha no processo: variancia menor que multiplicacao')

    def __format_result(self, variance: float) -> Dict:
        return {
            'data':{
                'Calculator': 3,
                'Variance': variance,
                'Success': True
            }
        }

    def calculate(self, request: FlaskRequest) -> Dict:
        """calculate"""
        body = request.json
        input_data = self.__validate_body(body)
        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        self.__verify_results(variance, multiplication)

        format_response = self.__format_result(variance)
        return format_response
