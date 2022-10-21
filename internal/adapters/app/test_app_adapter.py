from dataclasses import dataclass

from internal.adapters.app.app import Adapter
from internal.adapters.domain.arithmetic import ArithCore

arith = ArithCore()
app_adapter = Adapter(arithmetic=arith)


@dataclass
class MockData:
    A: int
    B: int
    Expected: int


def test_get_addition():

    mockData = [
        MockData(1, 2, 3),
        MockData(5, 3, 8),
        MockData(100, 800, 900),
        MockData(1234, 29022, 30256),
    ]

    for v in mockData:
        assert app_adapter.GetAddition(v.A, v.B) == v.Expected


def test_get_subtraction():

    mockData = [
        MockData(5, 2, 3),
        MockData(5, 3, 2),
        MockData(100, 800, -700),
        MockData(1234, 29022, -27788),
    ]

    for v in mockData:
        assert app_adapter.GetSubtraction(v.A, v.B) == v.Expected
 

def test_get_multiplication():

    mockData = [
        MockData(5, 2, 10),
        MockData(5, 3, 15),
        MockData(100, 800, 80000),
        MockData(1234, 29022, 35813148),
    ]

    for v in mockData:
        assert app_adapter.GetMultiplication(v.A, v.B) == v.Expected


def test_get_division():

    mockData = [
        MockData(5, 2, 2.5),
        MockData(5, 3, 5/3),
        MockData(100, 800, 0.125),
        MockData(1234, 29022, 1234/29022),
    ]

    for v in mockData:
        assert app_adapter.GetDivision(v.A, v.B) == v.Expected
