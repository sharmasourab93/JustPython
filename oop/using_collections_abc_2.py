"""
Python: Inherting collections.abc for custom Container Types
Reference: Effective Python by Brett Slatkin
"""


# You want to provide sequence semantics for a binary tree class
# How do you make this act like a sequence type?
class BinaryNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        

# To make BinaryNode class act like a sequence,
# you can provide custom implementation of __getitem__

class IndexableNode(BinaryNode):
    def _search(self, count, index):
        # return (found, count)
        pass
    
    def __getitem__(self, index):
        found, _ = self._search(0, index)
        if not found:
            raise IndexError("Index Out of Range")
        
        return found.value

# The problem is that implementing __getitem__ isn't enough to provide
# all of the sequence semantics you'd expect.
        
if __name__ == '__main__':
    tree = IndexableNode(
        10,
        left=IndexableNode(
            5,
            left=IndexableNode(
                6, right=IndexableNode(7)
                )
            ),
        right=IndexableNode(
            15,
            left=IndexableNode(11)
            )
        )
    
    print('LRR  =', tree.left.right.right.value)
    print("Index 0 = ", tree[0])
    print("Index 1 = ", tree[1])
    print("11 in the tree?", 11 in tree)
    print("17 in the tree?", 11 in tree)
    print("Tree is", list(tree))

# TODO: Revisit Needed.
# Things to remember

# 1. Inherit directly from python's container types
# (like list or dict) for simple cases

# 2. Beware of the large number o methods required to implement
# custom container types correctly

# 3. Have your custom container types inherit from interfaces
# defined in collections.abc to ensure that you classes match
# required interfaces and behaviors.
