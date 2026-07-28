from flask import request as FlaskRequest
import math

class Calculator1:

    """
    The first part is divided by 4, and the result is added to 7.
    After that, the result is squared and multiplied by a value of 0.257

    A segunda parte é elevada a pontência de 2.121, dividida por 5 e somado a 1


    A terceira parte se mantem no mesmo valor.

    """
    

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)

        splited_number = input_data / 3

        first_process_result = self.__first_process(splited_number)
        second_process_result = self.__second_process(splited_number)
        calc_result = first_process_result + second_process_result + splited_number
        response = self.__format_response(calc_result)

        return response

    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise Exception("Bad request")

        input_data = body["number"]
        return input_data

    
    def __first_process(self, first_number: float) -> float:
        return (((first_number / 4) + 7) * 0.257)


    def __second_process(self, first_process_number: float) -> float:
        return (((math.pow(first_process_number, 4)) / 5) + 1)

    def __format_response(self, calc_result: float) -> Dict:
        return {
            "data": {
                "Calculator": 1,
                "result": calc_result
            }
        }
    

    

        