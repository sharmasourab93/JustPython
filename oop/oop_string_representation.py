"""
Python: __repr__ Vs. __str__

        Main Points:
        __repr__ goal is to be unambiguous
        __str__ goal is to be readable
        Container’s __str__ uses contained objects’ __repr__

Reference:
https://stackoverflow.com/questions/1436703/difference-between-str-and-repr
"""


class Test:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Official string representation of an object
    def __repr__(self):
        return "Test a:{} b:{}".format(self.a, self.b)

    # Informal string representation of an object
    def __str__(self):
        return "From str method of Test: a is %s," "b is %s"%(self.a,self.b)


if __name__ == '__main__':
    test_obj = Test(1234, 5678)

    # This calls __str__()
    print(test_obj)

    # This calls __repr__()
    print([test_obj])