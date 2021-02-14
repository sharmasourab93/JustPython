"""
Python: Initialize parent class with super()
Reference: Effective Python by Brett Slatkin
"""


class MyBaseClass:
    def __init__(self, value):
        self.value = value


class TimesFive(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value *= 5
        

class PlusTwo(MyBaseClass):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        self.value += 2
        

class ThisWay(TimesFive, PlusTwo):
    def __init__(self, value):
        TimesFive.__init__(self, value)
        PlusTwo.__init__(self, value)


if __name__ == '__main__':
    foo = ThisWay(5)
    print("Should be (5 * 5) + 2 = 27 but is", foo.value)
    # The output should be 27 because (5*5) + 2 = 27.
    # But the call to the second parent class's constructor,
    # PlusTwo.__init__, causes self.value to be reset back to 5
    # when MyBaseClass.__init__ gets called a second time.
