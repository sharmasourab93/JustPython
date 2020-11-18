"""
Python: Decorator Pattern in Python
        A Decorator Example 9
        Chaining Decorators
        Source: dev.to
(https://dev.to/apcelent/python-decorator-tutorial-with-example-529f)
"""


def make_bold(f):
    return lambda: "<b>" + f() + "</b>"


def make_italic(f):
    return lambda: "<i>" + f() + "</i>"


@make_bold
@make_italic
def say():
    """
    The order of decorators we set matters.
    When you chain decorators,
    the order in which they are stacked is bottom to top.
    """
    return "Hello"


if __name__ == '__main__':
    print(say())
