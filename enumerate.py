"""
Python: Using Enumerate
"""


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    enum_arr = enumerate(arr)
    print("Type of Enumerate: ", type(enum_arr))

    print("Elements in Enumerate and its type")

    for i in enum_arr:
        print(i, "\t\t", type(i))