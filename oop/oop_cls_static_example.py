"""
Python: Object Oriented Programming
        Class & Static Methods in OOP
"""
from datetime import date


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, year):
        return cls(name, date.today().year-year)

    @staticmethod
    def is_adult(age):
        return age > 18


if __name__ == '__main__':

    person1 = Person('Mayank', 21)
    person2 = Person.from_birth_year('Myank', 1996)

    print(person1.age, person1.name)
    print(person2.age, person2.name)

    print(Person.is_adult(22))