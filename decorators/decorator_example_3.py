"""
Python: Decorator Pattern In Python
        A Decorator Example 3
        Using Decorators with Arguments
"""


def outer(func):
    def inner(*args):
        print("Inside the decorated function", args)
        return func(*args)
    return inner


@outer
def decorated(name):
    print("In the decorated function: arg {0}".format(name))


"""
The code above is equivalent to:
outter(decorated)("Bob")
decorated is replaced with the return value of outer(decorated) (which is inner).
When you call decorated, you’re actually calling inner.
"""
    
    
if __name__ == '__main__':
    decorated('Sourab')
    print(decorated)
