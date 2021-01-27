"""
Python: Pytest
        Pytest 101
        Learning pytest with Examples
        Calculator Class's PyTest File test_calculator.py
"""


from numbers import Number
from sys import exit


class CalculatorError(Exception):
    """An Exception class for calculator."""


class Calculator:
    """A Terrible Calculator."""
    
    def add(self, x, y):
        try:
            self._check_operand(x)
            self._check_operand(y)
            return x + y
        except TypeError:
            raise CalculatorError('Wrong')
        
    def subtract(self, x, y):
        return x - y
        
    def multiply(self, x, y):
        return x * y
    
    def _check_operand(self, operand):
        if not isinstance(operand, Number):
            raise CalculatorError(f'"{operand}" was not a number')


if __name__ == '__main__':
    calculator = Calculator()
    operations = [
        calculator.add,
        calculator.subtract,
        calculator.multiply
        ]
    
    print("Let's calculate!")
    
    while True:
        print("Pick an operation")
        for i in enumerate(operations, start=1):
            print(f"{i[0]}: {i[1].__name__}")
        print("q for quit")
        operation = input("Pick an operation:")
        
        if operation == 'q':
            exit()
        
        op = int(operation)
        a, b = input("What is a & b?").split()
        a, b = int(a), int(b)
        result = operations[op - 1]
        print(result(a, b))
