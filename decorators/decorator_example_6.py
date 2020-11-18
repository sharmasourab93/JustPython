"""
Python: Decorator Pattern in Python
        A Function Example 6
        A Class Decorator
        Source: dev.to
(https://dev.to/apcelent/python-decorator-tutorial-with-example-529f)
"""


import time


def timetest(input_func):
    
    def timed(*args, **kwargs):
        
        start_time = time.time()
        result = input_func(*args, **kwargs)
        end_time = time.time()
        timed_result = end_time - start_time
        
        print("Method Name - {0},\n Args - {1},\n "
              "Kwargs - {2},\n Exec. Time - {3}"
              .format(input_func.__name__,
                      args,
                      kwargs,
                      round(timed_result, 2))
              )
    
        return result
    
    return timed


@timetest
def foobar(*args, **kwargs):
    time.sleep(0.3)
    print("Inside foobar")
    print(args, kwargs)
    
    
if __name__ == '__main__':
    foobar(["hello, world"], foo=2,  bar=5)
