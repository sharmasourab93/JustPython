"""
Python : Generator Functions
         Yield Key Word
"""

# https://stackoverflow.com/questions/42983569/how-to-write-a-generator-class


# Example 1: To Generate the next square
def next_square():
    i = 1
    while i < 10 and True:
        # Returns the value of i*i
        yield i * i
        # Returns i+2 value in next iteration
        i = i + 2


# Example 2: Sample Generator Method
def sample_generator():
    i = 1
    while i < 7 and True:
        # Retains value of i
        # Unlike a method
        yield i * i
        i += 1


if __name__ == '__main__':
    print("In next_square")
    num = int()
    for num in next_square():
        if num > 15:
            break

    print(num)

    print("In sample_generator")
    for i in sample_generator():
        print(i)
