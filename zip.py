"""
Python: Zip
"""

if __name__ == '__main__':
    # Using Zip
    print("Using Zip")

    array = [1, 2, 3, 4, 5]
    name = ["Sourab", "Amit", "Himesh"]

    # The extra elements are truncted
    # in the zipped container
    zipped_list = list(zip(array, name))

    print("Array", array)
    print("Name list", name)
    print("On Zipping", zipped_list)
