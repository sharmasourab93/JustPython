"""
Python: Use Plain Attributes Instead of Get & Set Methods
Resource: Effective Python by Brett Slatkin
"""


# class OldResistor:
#
#     def __init__(self, ohms):
#         self._ohms = ohms
#
#     def get_ohms(self):
#         return self._ohms
#
#     def set_ohms(self, ohms):
#         self._ohms = ohms

# Using these settings and getters is simple, but it's not Pythonic.
# r0 = OldResistor(50e3)
# print("Before: %5r" % r0.get_ohms())
# r0.set_ohms(10e3)
# print("After: %5r" % r0.get_ohms())

# These utility methods do help define the interface for your class,
# making it easier to encapsulate functionality, validate usage,
# and define boundaries. Those are important goals
# when designing a class to ensure you don't break callers
# as your classes evolves over time.

class Resistor:
    def __init__(self, ohms):
        self.ohms = ohms
        self.voltage = 0
        self.current = 0
        
r1 = Resistor
