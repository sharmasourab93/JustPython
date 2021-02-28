"""
Python: Inherting collections.abc for custom Container Types
Reference: Effective Python by Brett Slatkin
"""


# Every Python Class is a container of some kind,
# encapsulating attributes and functionality together.
# Python also provides built-in container types for managing data:
# lists, tuples, sets & dictionaries

# For Example: Creating Lists with additional method
# of counting the Frequence of the members.
class FrequenceList(list):
    def __init__(self, members):
        super().__init__(members)
        
    def frequency(self):
        counts = {}
        for item in self:
            counts.setdefault(item, 0)
            counts[item] += 1
            
        return counts
    
    """
    By sub-classing List,
    you get all the standard functionality of a list
    and preserve the semantics familiar to all Python Programmers.
    Your aditional methods can add any customer behaviour you  need.
    """
    

if __name__ == '__main__':
    foo = FrequenceList(['a', 'b', 'a', 'c', 'b', 'a', 'd'])
    print("Length is {0}".format(len(foo)))
    foo.pop()
    print("After pop: {0}".format(repr(foo)))
    print("Frequency: {0}".format(foo.frequency()) )
