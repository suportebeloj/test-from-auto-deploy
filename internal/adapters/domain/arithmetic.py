from internal.ports.arithmentic import ArithInterface


class ArithCore(ArithInterface):

    def addition(self, a, b):
        return a + b

    def subtraction(self, a, b):
        return a - b
    def multiplication(self, a, b):
        return a * b
    
    def subtraction(self, a, b):
        return a / b