"""Content of the calculator_1.py file"""
from typing import Dict
from flask import request as FlaskRequest

class Calculator1:
    """ASdas """

    def __validate_body(self, body: Dict) -> float:
        """Validar corpo"""
        if 'number' not in body:
            raise ValueError('body mal formatado')

        input_data = float(body['number'])
        return input_data

    def __first_process(self, first_number: float) -> float:
        """Primeira etapa"""
        first_part = (first_number / 4) + 7
        second_part = (first_part ** 2) * 0.257
        return second_part

    def __second_process(self, second_number: float) -> float:
        """Segundo processo"""
        first_part = second_number ** 2.121
        second_part = (first_part / 5) + 1
        return second_part

    def __format_response(self, calc_result: float) -> Dict:
        return {
            "data": {
                "Calculator": 1,
                "Result": round(calc_result, 2)
            }
        }

    def calculate(self, request: FlaskRequest) -> Dict:
        """Execução"""
        body = request.json
        input_data = self.__validate_body(body)
        splited_number = input_data / 3

        first_process_result = self.__first_process(first_number=splited_number)
        second_process_result = self.__second_process(second_number=splited_number)
        calc_result = first_process_result + second_process_result + splited_number
        response = self.__format_response(calc_result)

        return response
