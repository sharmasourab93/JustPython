"""
Python: Decorator Pattern in Python
        A Decorator Example 11
        Class based Decorators with Arguments
        Source: dev.to
(https://dev.to/apcelent/python-decorator-tutorial-with-example-529f)
"""


class ClassDecorator:
    
    def __init__(self, arg1, arg2):
        
        print("Arguments passed to decorators {0} and {1}"
              .format(arg1, arg2))
        self.arg1 = arg1
        self.arg2 = arg2
        
    def __call__(self, foo, *args, **kwargs):
        
        def inner_func(*args, **kwargs):
            print("Args passed inside decorated function {0} and {1}"
                  .format(self.arg1, self.arg2))
            return foo(*args, **kwargs)
        
        return inner_func
    

@ClassDecorator("Str-arg1", "Str-arg2")
def print_args(*args):
    for arg in args:
        print(arg)
        

if __name__ == '__main__':
    print_args(1, 2, 3)
