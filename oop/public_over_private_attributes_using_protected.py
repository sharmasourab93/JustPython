"""
Python: Using Public Attributes over
        Private Attributes by using protected classes
Reference: Effective Python by Brett Slatkin
"""


# In general it is better to err on the side of allowing
# subclasses to do more by using protected attributes.

# Document each protected field and
# explain which are internal APIs available to subclasses and
# which should be left alone entirely.

class MyClass:
    def __init__(self, value):
        self._value = value
        

class ApiClass:
    def __init__(self):
        # protected member
        self._value = 5
        
    def get(self):
        return self._value


class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello' # conflicts
        
        
# this is primarily a concern w ith classes that
# are part of a public API; subclasses are out of your control
# To reduce the risk of this happening, you can use a private attribute
# in the parent class to ensure that there are no attribute names that
# overlap with child classes.

class NewApiClass:
    def __init__(self):
        self.__value = 5
        
    def get(self):
        return self.__value
    

class NewChild(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello' # OK
        

if __name__ == '__main__':
    a = Child()
    print(a.get(), 'and', a._value, "should be different")
    b = NewChild()
    print(f"{b.get()} and {b._value} are different")
    print(b.__dict__)
    
    
# Things to remember
# 1. Private attributes aren't rigourously
# enforced by the Python compiler.
# 2. Plan from the beginning to allow subclasses to do more
# with your internal APIs and attributes instead of locking
# them out by default
# 3. Use documentation of protected fields to guide subclasses
# instead of trying to force access control with private attributes
# 4. Only consider using private attributes to avoid naming conflicts
# with subclasses that are out of your control.
