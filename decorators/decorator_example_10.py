"""
Python: Decorator Pattern in Python
        A Decorator Example 10
        Func tools & Wrappers
        Source: dev.to
(https://dev.to/apcelent/python-decorator-tutorial-with-example-529f)
"""


from functools import wraps


def wrapped_decorator(func):
    
    """Wrapped Decorator Docstring"""
    
    """
    functools.wraps comes to our rescue in preventing
     the function from getting replaced.
    It takes the function used in the decorator
     and adds the functionality of copying over
    the function name, docstring, arguemnets etc.
    """
    
    @wraps(func)
    def inner_function(*args, **kwargs):
        """Inner Function Docstring"""
        
        print(f"{func.__name__} was called")
        return func(*args, **kwargs)
    
    return inner_function


@wrapped_decorator
def foobar(x):
    """Foobar Docstring"""
    return x**2


if __name__ == '__main__':
    print(foobar.___name__)
    print(foobar.__doc__)
