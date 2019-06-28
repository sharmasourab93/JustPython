"""
Python: Object Oriented Programming
        Data Hiding
"""


class MyClass:

    #Hidden with __
    __hidden = 0

    def add(self, increment):

        self.__hidden += increment

        print(self.__hidden)


if __name__ == '__main__':
    my_class_obj = MyClass()
    my_class_obj.add(2)
    my_class_obj.add(10)

    # To print the hidden members of the class
    print(my_class_obj._MyClass__hidden)