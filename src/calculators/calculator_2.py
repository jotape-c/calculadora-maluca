"""Second calculador"""
from typing import Dict, List
from flask import request as FlaskRequest

from src.drivers.interfaces.driver_handler_interface import DriverHandleInterface

class Calculator2:
    """
    Regras:
    1. n números são enviados
    2. todos esses n números são multiplicados por 11 e elevado a potencia de 0,95
    3. por fim, é retidado o devio padrão desses resultados e retornado o inverso desse valor (1/resultado)
    """
    def __init__(self, driver_handler: DriverHandleInterface) -> None:
        self.__driver_handler = driver_handler

    def __validate_body(self, body: Dict) -> List[float]:
        """Validar body"""
        if 'numbers' not in body:
            raise TypeError('body mal formatado')

        input_data = body['numbers']
        return input_data

    def __process_data(self, input_data: List[float]) -> float:
        """"""
        numbers = [(num * 11) ** 0.95 for num in input_data]
        result = self.__driver_handler.standard_derivation(numbers)
        return float(1/result)

    def calculate(self, request: FlaskRequest) -> Dict:
        "execute calc"
        body = request.json
        input_data = self.__validate_body(body)
        result = self.__process_data(input_data)

        return {
            'data': {
                'Calculator': 2,
                'Result': result
            }
        }
