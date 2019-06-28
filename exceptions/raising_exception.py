"""
Python: Exceptions
        Raising Exceptions
"""


class ShortInputException(Exception):
    def __init__(self, length, atleast):

        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


if __name__ == '__main__':
    try:
        text = input('Enter Something--->')
        if len(text) < 3:
            raise ShortInputException(len(text), 3)

    except EOFError:
        print('Why did you do an EOF on me?')

    except ShortInputException as short_exception:
        print('ShortInputException: The input was' +
              '{0} long, expected at least {1}'
              .format(short_exception.length, short_exception.atleast))

    else:
        print('No exception was raised')