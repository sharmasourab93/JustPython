"""
Python: Object Oriented Programming
        Usage of Static Methods: Isolated or contained

        Static methods act as separate utility functions without internal
        reference to self in a class.
        But they can be invoked using the Class name only
"""


class Foo:

    lol = 10

    def __init__(self):
        self.bar = 'barry'

    def too(self):
        return self.bar

    @staticmethod
    def foo(bar):
        # Static method cannot access
        # internal members of the class
        # print(self.bar) throws an error
        print("Static prints "+bar)


if __name__ == '__main__':
    obj = Foo()
    # Parameter passed to static method
    # using an instance obj method call
    obj.foo(obj.too())

    # Static method returns the string
    # passed as a parameter
    Foo.foo("Ola")