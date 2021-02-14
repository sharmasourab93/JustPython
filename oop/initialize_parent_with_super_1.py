"""
Python: Initialize parent class with super()
Reference: Effective Python by Brett Slatkin
"""


# Old way to initialize Parent class from Child class
# This approach works fine for simple hierarchies
# but breaks down in many cases.
# If your class is affected by multiple inheritance(avoided in general)
# calling the superclasses' __init__ methods directly
# can lead to unpredictable behaviour.
class MyBaseClass:
    def __init__(self, value):
        self.value = value
        

class MyChildClass(MyBaseClass):
    def __init__(self):
        MyBaseClass.__init__(self, 5)


class TimesTwo:
    def __init__(self):
        self.value *= 2
        

class PlusFive:
    def __init__(self):
        self.value += 5
        

class OneWay(MyBaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


# Order Changes in contrast to class OneWay
class AnotherWay(MyBaseClass, PlusFive, TimesTwo):
    def __init__(self, value):
        MyBaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


if __name__ == '__main__':
    foo = OneWay(5)
    print("First Ordering is ( 5 * 2 ) + 5 = ", foo.value)
    
    bar = AnotherWay(5)
    print("Second ordering still is", bar.value)
