"""
Python: Using Public Attributes over
        Private Attributes With Inheritance
Reference: Effective Python by Brett Slatkin
"""


# As you'd expect with private fields,
# a subclass can't access it's parent class's private fields.
class MyParentObject:
    def __init__(self):
        self.__private_field = 71
        

class MyChildObject(MyParentObject):
    def get_private_field(self):
        return self.__private_field
    
    
if __name__ == '__main__':
    baz = MyChildObject()
    try:
        print(baz.get_private_field())
    except AttributeError as e:
        # noinspection PyCompatibility
        print(f"Attribute Error: {e}")
    
    print(baz.__dict__)
