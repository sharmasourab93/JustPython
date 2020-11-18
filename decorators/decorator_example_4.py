"""
Python: Decorator Pattern In Python
        A Decorator Example 4
        Using Decorators with Parameter
        Source: Geeksforgeeks.org
"""


def decorator_fun(func):
    print("Inside Decorator")
    
    def inner(*args):
        print("Inside inner Function")
        print("Decorated the Function")
        print("Printing args:", None if args is None else args)
        func()
        
    return inner


@decorator_fun
def func_to():
    print("Inside actual function ")
    

"""
The code above is equivalent to:
    decorator_fun(func_to)()
"""
    
    
if __name__ == '__main__':
    func_to()
