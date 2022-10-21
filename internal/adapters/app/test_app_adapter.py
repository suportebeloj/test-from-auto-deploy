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
