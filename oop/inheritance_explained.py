"""
Python: Object Oriented Programming
        Inheritance Example
        Source: Geeks4geeks
"""


class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def is_employee(self):
        return False


class Employee(Person):

    # For every new Employee instance
    # Overrides is_employee method in Person
    def is_employee(self):
        return True


if __name__ == '__main__':
    # Person 1 Geeks 1
    emp = Person("Geeks1")
    print("Person's Name", emp.get_name())
    print("Is Person an Employee?", emp.is_employee())

    # isinstance explained
    print("Is Person 1 an isinstance of Employee", isinstance(emp, Employee), end="\n\n")

    # Person 2 Employee 1 Geeks 2
    emp1 = Employee("Geeks2")
    print("Person's Name", emp1.get_name())
    print("Is Person 2 an Employee?", emp1.is_employee())

    # isinstance explained
    # Since Employee inherits Person, arguments passed to
    # Employee is implemented from the inherited class
    print("Is person 2 an isinstance of Employee", isinstance(emp1, Employee))
    print("Is person 2 an isinstance of Person", isinstance(emp1, Person))