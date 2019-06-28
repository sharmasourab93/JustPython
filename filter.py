"""
Python: Filter
        Pre-requisite lambda & map
"""


# Function to find square of a number
def square(x):
    return x**2


# Function to find cube of a number
def cube(x):
    return x**3


if __name__ == '__main__':

    # Filter Examples
    print("Using filter ")

    print("\nExample 1")
    cube_map = list(map(cube, range(10)))
    filter_cube = filter(lambda x: 1 < x < 216, cube_map)
    print("Mapped Cube function list", cube_map)
    print("Filtered list 1 < x < 100:", list(filter_cube))

    print("\nExample 2")
    square_map = list(map(square, range(10)))
    filter_square = filter((lambda x: 16 < x < 100), square_map)
    print("Mapped Square function list", square_map)
    print("Filtered List 16 < x < 100:", list(filter_square))