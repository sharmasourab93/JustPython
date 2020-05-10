"""
Python: ENUM (Enumeration)
        An enum (enumeration) is a set of symbolic names
        bound to unique constant values.

        Properties of enum:
          1. Enums can be displayed as string or repr.
          2. Enums can be checked for their types using type().
          3. “name” keyword is used to display the name of enum member.
          4. Enumerations are iterable. They can be iterated using loops
          5. Enumerations support hashing hence used in dict or sets.

        Accessing Modes: Enum members can be accessed by two ways
        1. By value: In this method, the value of enum member is passed.
        2. By name: In this method, the name of enum member is passed.

        Comparison: Enumerations supports two types of comparisons
        1. Identity: These are checked using keywords “is” and “is not“.
        2. Equality: Equality “==” and “!=” types are also supported.

Reference:
https://www.geeksforgeeks.org/enum-in-python/
"""
import enum


class Animal(enum.Enum):
    DOG = 1
    CAT = 2
    LION = 3


if __name__ == '__main__':
    print("The string representation of enum member is:", Animal.DOG)

    print("The string representation of enum member is:", repr(Animal.DOG))

    print("The type of enum member is:", type(Animal.DOG))

    print("The name of enum member is:", Animal.DOG.name)

    print("The value of enum is:", Animal.DOG.value)