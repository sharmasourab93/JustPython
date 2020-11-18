"""
Python: Decorator Pattern in Python
        A Decorator Example 8
        A Class Decorator
        Source: dev.to
(https://dev.to/apcelent/python-decorator-tutorial-with-example-529f)
"""


class DecoClass:
    
    """
    With a class,
    you can add methods and properties
    to the decorated callable object,
    or implement operations on them.
    You can create descriptors that act
    in a special way when placed in classes
    (e.g. classmethod, property)
    """
    
    def __init__(self, f):
        self.f = f
    
    def __call__(self, *args, **kwargs):
        print("Decorator Initialized")
        self.f(*args, **kwargs)
        print("Decorator Terminated")
        

@DecoClass
def klass():
    print("Inside Class Method")
    

if __name__ == '__main__':
    klass()
