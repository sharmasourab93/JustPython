"""
Python: Object Oriented Programming
        Functioning of Inheritance
"""


# Base Class
class SchoolMember:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized School Member: {})'.format(self.name))

    def tell(self):
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


# Derived Class A
class Teacher(SchoolMember):

    def __init__(self, name, age, salary):

        # Referring to parent __init__
        SchoolMember.__init__(self, name, age)

        self.salary = salary
        print('(Employed teacher:{})'.format(self.name), end="\n\n")

    def tell(self):
        SchoolMember.tell(self)

        print('Salary:"{}"'.format(self.salary))


# Derived Class B
class Student(SchoolMember):

    # __init__ overrides base class's __init__
    def __init__(self, name, age, marks):

        # Referring to parent __init__
        SchoolMember.__init__(self, name, age)

        self.marks = marks
        print('(Admitted Student:{})'.format(self.name), end="\n\n")

    def tell(self):
        SchoolMember.tell(self)

        print('Marks: {}'.format(self.marks))


if __name__ == "__main__":
    teacher_var = Teacher("Mrs. Shri Vidya", 40, 30000)
    student_var = Student("Sourab", 25, 80)

    members = [teacher_var, student_var]
    for mem in members:
        mem.tell()