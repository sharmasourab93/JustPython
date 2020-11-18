"""
Python: Decorator Pattern in Python
        A Decorator Example 7
        A Method Decorator
        Source: dev.to
(https://dev.to/apcelent/python-decorator-tutorial-with-example-529f)
"""


def method_decorator(method):
    
    def inner(city_instance):
        
        if city_instance.name == 'SFO':
            print("Its a Cool Place to live in.")
        else:
            method(city_instance)
    
    return inner


class City:
    
    def __init__(self, name):
        self.name = name

    """
    Method decorators allow overriding class properties
    by decorating,
    without having to find the calling function.
    """
    @method_decorator
    def print_test(self):
        print("Name of the city {0}".format(self.name))
        

if __name__ == '__main__':
    p1 = City("SFO")
    p2 = City("LGA")
    p1.print_test()
    p2.print_test()
