from internal.ports.app import APIInterface
from internal.ports.arithmentic import ArithInterface


class Adapter(APIInterface):

    def __init__(self, arithmetic: ArithInterface) -> None:
        self.arith = arithmetic

    def GetAddition(self, a, b):
        return self.arith.addition(a, b)

    def GetSubtraction(self, a, b):
        return self.arith.subtraction(a, b)

    def GetMultiplication(self, a, b):
        return self.arith.multiplication(a, b)

    def GetDivision(self, a, b):
        return self.arith.division(a, b)
