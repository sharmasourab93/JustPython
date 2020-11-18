"""
Python: Decorator Pattern in Python
        A Decorator Example 5
        Other ways to use Decorators
        Source: Geeksforgeeks.org
"""


def decorator_func(x, y):
    
    def inner(func):
        def wrapper(*args, **kwargs):
            print("Inside the Wrapper Function")
            print("Summation of values: {0}".format(x+y))
            
            func(*args, **kwargs)
            
        return wrapper
    return inner


@decorator_func(12, 15)
def my_fun(*args):
    for ele in args:
        print(ele)
        
        
"""
The above code can be written without decorators
in this format to spit out the same result:
decorator_func(12, 15)(my_fun)('Geeks', 'for', 'Geeks')
"""
        
        
if __name__ == '__main__':
    my_fun('Sourab', 'S', 'Sharma')
