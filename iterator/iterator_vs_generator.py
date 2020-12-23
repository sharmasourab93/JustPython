"""
Python: Iterator Vs Generator
"""


def my_generator():
    for i in range(10):
        yield i


# Functions that accept *args are best
# for the situations where you know the number of inputs
# in the arguments list will be reasonably small.
# Using * operator with a generator
# may cause your program to run out of memory and crash.w
def my_func(*args):
    print(args)
    # x, *y = args
    # print(x,  y)
    
    
if __name__ == '__main__':
    it = my_generator()
    my_func(*it)
