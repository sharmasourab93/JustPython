"""
Python: Object Oriented Programming
        Inheritance: Corey Schafer's Example
"""


# Base Class
class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first+'.'+last+'@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


# Derived Class A
class Developer(Employee):

    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)

        self.prog_lang = prog_lang


# Derived Class B
class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)

        if employees is None:
            self.employees = []

        else:
            self.employees = employees

    def add_emp(self, emp):

        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):

        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):

        for emp in self.employees:
            print('-->', emp.fullname())

    # Official string representation of an object
    def __repr__(self):
        return "Employee('{}','{}','{}')".format(self.first, self.last, self.pay)

    # Informal string representation of an object
    def __str__(self):
        return '{}-{}'.format(self.fullname(), self.email)


if __name__ == '__main__':
    dev1 = Developer('Sourab', 'Sharma', 50000, 'Python')
    dev2 = Developer('Test', 'Employee', 60000, 'Java')

    print(Developer.apply_raise(dev1))
    print(dev1.fullname())

    mgr1 = Manager('Shri', 'Balaji', 90000, [dev1])
    print(mgr1)

    mgr1.add_emp(dev2)
    mgr1.remove_emp(dev1)
    mgr1.print_emp()
