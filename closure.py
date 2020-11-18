"""
Python : Closure Example
"""


def outer_function(text):
    def inner_function():
        print(text)
    
    return inner_function

def assign_lambda():
    return lambda x: not x == x


if __name__ == '__main__':
    my_function = outer_function('Hey!')
    my_function()
    outer_function('hello')
    
    # lambda x: not x == x
    foo = assign_lambda()
    print(foo('asdf'))
    print(foo(float('nan')))
