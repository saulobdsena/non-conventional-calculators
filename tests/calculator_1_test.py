
from src.calculators.calculator_1 import Calculator1
from typing import Dict
from pytest import raises, approx

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():

    mock_request = MockRequest(body={ "number" : 1})

    calculator = Calculator1()

    response = calculator.calculate(mock_request)
    
    assert "data" in response
    assert "Calculator" in response['data']
    assert "result" in response["data"]

    assert response["data"]["result"] == approx(14.24740748999224)

def test_calculate_with_body_error():
    mock_request = MockRequest(body={ "something" : 1})

    calculator = Calculator1()

    with raises(Exception) as excinfo:
        calculator.calculate(mock_request)


    assert str(excinfo.value) == "Bad request"


