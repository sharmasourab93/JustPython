"""
Python: lambda functions
"""


if __name__ == '__main__':

    print("Using lambda functions")

    # First parentheses contains a lambda form that is
    # a squaring function and second parentheses represents
    # calling lambda
    print("Example 1", (lambda x: x**2)(5))
    print("Example 2", (lambda x, y: x*y)(3, 4))

    lambda_store = (lambda x: x**2)(5)
    print("Example 3", lambda_store)