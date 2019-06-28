"""
Python: map
"""


# Function to find square of a number
def square(x):
    return x**2


# Function to find cube of a number
def cube(x):
    return x**3


if __name__ == '__main__':
    # Using map
    print("Using Maps")

    # Example 1
    print("Example 1")
    for i in map(square, range(10)):
        print(i, end=" ")

    # Example 2
    print("\nExample 2")
    cube_map = map(cube, range(10))
    for x in cube_map:
        print(x, end=" ")