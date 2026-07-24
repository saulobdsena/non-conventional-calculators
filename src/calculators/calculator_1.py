from flask import request as FlaskRequest

class Calculator1:

    """
    The first part is divided by 4, and the result is added to 7.
    After that, the result is squared and multiplied by a value of 0.257
    """
    

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        print(input_data)
    
    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise Exception("Body mal formatado")

        input_data = body["number"]
        return input_data



print("TESTE DO COMMIT")