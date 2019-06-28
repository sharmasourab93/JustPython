"""
Python : Exceptions
         Defining Exceptions
"""


class MyError(Exception):
    def __init__(self, value):
        self.value = value

    # __str__ is to print() the value
    def __str__(self):
        return repr(self.value)


if __name__ == '__main__':
    try:
        raise(MyError(3*2))

    except MyError as error:
        print('A new Exception occured: ', error.value)