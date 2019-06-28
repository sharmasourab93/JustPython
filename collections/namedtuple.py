"""
Python: Using collections.namedtuple
        getattr
"""
from collections import namedtuple


if __name__ == '__main__':
    student = namedtuple('Student', ['name', 'age', 'DOB'])
    s = student('Nandini', '19', '2541997')
    print("The student age using index is:", s[1])

    #Access using name
    print("The student age using keyname is:", s.name)

    #Access using getattr()
    print("The student DOB using getattr() is: ", getattr(s, 'DOB'))