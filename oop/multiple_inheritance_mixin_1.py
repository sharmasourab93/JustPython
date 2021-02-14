"""
Python: Use Multiple Inheritance Only for Mix-in Utility Class
"""


from pprint import pprint


# If you find yourself desiring the convenience and
# encapsulation that comes with multiple inheritance,
# consider writing a mix-in instead.

# A Mix-in is a small class that only defines a set of
# additional methods that a class should provide.
# Mix-in classes don't define their own instance attributes
# nor require their __init__ constructor to be called.

# Writing Mix-ins is easy because Python makes it trivial
# to inspect the current state of any object regardless of its type.
# Dynamic inspection lets you write generic functionality a single time
# in a mix-in, that can be applied to many other classes.
# Mixins can be composed and layered to minimize
# repetitive code and maximize reuse.

# here is an example mix-in that accomplishes this with
# a new public method that's added to any class that inherits from it
class ToDictMixin:
    def to_dict(self):
        return self._traverse_dict(self.__dict__)
    
    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
            
        return output
    
    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value


# Translating a large number of related python objects
# into a dictionary becomes easy.
class BinaryTree(ToDictMixin):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# The best part about mixins is that you can make their
# generic functionality pluggable so behaviors
# can be overridden when required.

# Definish BinaryTree that holds areference to its parent.
# This curcular reference would cause the default implemetation
# of ToDictMixin.to_dict to loop forever.
class BinaryTreeWithParent(BinaryTree):
    def __init__(self, value, left=None, right=None, parent=None):
        super().__init__(value, left=left, right=right)
        self.parent = parent
        
    def _traverse(self, key, value):
        # By defining this function, any class that has an attribute
        # of type BinaryTreeWithParent is enabled
        # to automatically work with ToDictMixin
        if isinstance(value, BinaryTreeWithParent) and key == 'parent':
            return value.value # Prevent Cycles
        
        else:
            return super()._traverse(key, value)
        
        
class NamedSubTree(ToDictMixin):
    def __init__(self, name, tree_with_parent):
        self.name = name
        self.tree_with_parent = tree_with_parent


if __name__ == '__main__':
    tree = BinaryTree(10,
                      left=BinaryTree(7, right=BinaryTree(9)),
                      right=BinaryTree(13, left=BinaryTree(11)))
    pprint(tree.to_dict())
    
    # Binary Tree with Parent
    root = BinaryTreeWithParent(10)
    root.left = BinaryTreeWithParent(7, parent=root)
    root.left.right = BinaryTreeWithParent(9, parent=root.left)
    pprint(root.to_dict())
    
    # NamedSubTree
    my_tree = NamedSubTree('foobar', root.left.right)
    pprint(my_tree.to_dict()) # No Infinite Loop
