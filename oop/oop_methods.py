"""
Python: Object Oriented Programming
        Difference between Self, Cls, Static
"""


class MyClass:

    def method(self):
        return 'instance method called', self

    @classmethod
    def class_method(cls):
        return 'cls method called', cls

    @staticmethod
    def static_method():
        return 'static method called'


if __name__ == "__main__":
    m = MyClass()

    print(m.method())
    print(m.class_method())

    print(MyClass.class_method(), MyClass.class_method)

    print(MyClass.static_method(), MyClass.static_method)
    print(m.static_method(), m.static_method)

    # TypeError: method() missing 1 required positional argument: 'self'
    # MyClass.method()