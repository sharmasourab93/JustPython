"""
Python: Object Oriented Programming
        Class Member Access
"""


class CSStudent:

    # Class Variable
    stream = 'cse'

    def __init__(self, name, roll):
        self.name = name
        self.roll = roll


if __name__ == '__main__':
    a = CSStudent("Geek", 1)
    b = CSStudent("Nerd", 2)

    print("Initially")

    print("a.stream= " + a.stream)
    print(a.name, a.roll)

    print("b.stream= " + b.stream)
    print(b.name, b.roll, end="\n\n")

    CSStudent.stream = "Cse"
    # Changes the particular instance's stream name
    a.stream = "ece"

    print("Later")
    print("a.stream= " + a.stream)
    print(a.name, a.roll)

    print("b.stream= " + b.stream)
    print(b.name, b.roll, end="\n\n")

    print(CSStudent.stream)

    print("\nPost Action ")
    # Changes the class variable
    CSStudent.stream = "mec"
    print("a.stream= " + a.stream)
    print(a.name, a.roll)
    print("b.stream= " + b.stream)
    print(b.name, b.roll)
