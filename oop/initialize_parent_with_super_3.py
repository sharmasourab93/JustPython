"""
Python: Initialize parent class with super()
Reference: Effective Python by Brett Slatkin
"""
from pprint import pprint


class MyBaseClass:
    def __init__(self, value):
        print(__class__)
        self.value = value
        print(self.value)
        

class TimesFiveCorrect(MyBaseClass):
    def __init__(self, value):
        print(__class__)
        super(__class__, self).__init__(value)
        self.value *= 5
        print(self.value)


class PlusTwoCorrect(MyBaseClass):
    def __init__(self, value):
        print(__class__)
        super(__class__, self).__init__(value)
        self.value += 2
        print(self.value)
        

class GoodWay(TimesFiveCorrect, PlusTwoCorrect):
    def __init__(self, value):
        super(__class__, self).__init__(value)
        

if __name__ == '__main__':
    foo = GoodWay(5)
    print("Should be 5 * (5 + 2) = 35 and is ", foo.value)
    pprint(GoodWay.mro())
# Things to remember
# Python's standard method resolution order (MRO) solves the
# problems of superclass initialization order and diamond inheritance
# Always use the super built-in function to initialize parent classes
