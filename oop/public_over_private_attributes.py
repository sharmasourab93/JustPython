"""
Python: Using Public Attributes over Private Attributes
Reference: Effective Python by Brett Slatkin
"""


class MyObject:
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10
        
    def get_private_field(self):
        return self.__private_field
    
    @classmethod
    def get_private_field_of_instance(cls, instance):
        return instance.__private_field
    
    
if __name__ == '__main__':
    foo = MyObject()
    assert foo.public_field == 5
    assert foo.get_private_field() == 10
    # Directly accesssing private fields from outside the class
    # raises an exception.
    try:
        print(foo.__private_field)
    except AttributeError as e:
        # noinspection PyCompatibility
        print(f"Attribute error: {e}")
    
    assert foo.get_private_field_of_instance(foo) == 10