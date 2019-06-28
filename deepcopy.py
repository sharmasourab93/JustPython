"""
Python: Copy
        Deep Copy Vs Shallow Copy
"""
import copy


def deep_copy(array1):

    array2 = copy.deepcopy(array1)

    print("The original elements before deep copying")
    for i in range(0, len(array1)):
        print(array1[i], end=" ")

    print('\r')

    array2[2][0] = 7

    # change reflected in l2
    print("the new lis tof elements after deep copying")
    for i in range(0, len(array1)):
        print(array2[i], end=" ")

    print("\r")

    print("The original elements after deep copying")
    for i in range(0, len(array1)):
        print(array1[i], end=" ")


def shallow_copy(array1):
    array2 = copy.copy(array1)
    print("The original elements before shallow copying")
    for i in range(0, len(array1)):
        print(array1[i], end=" ")

    array2[2][0] = 7
    print("The original elements after shallow copying")
    for i in range(0, len(array1)): print(array1[i], end=" ")


if __name__ == '__main__':
    array1 = [1, 2, [3, 5], 4]
    shallow_copy(array1)
    deep_copy(array1)

