"""
Python: Using __slots__ to Store Object Data in Python

Reference: https://stackabuse.com/using-slots-to-store-object-data-in-python/
"""


# Dictionaries can consume a fair chunk of memory,
# especially if we have many instance objects with
# a large number of attributes.
# If the performance and memory efficiency of code are critical
# we can trade the convenience of dictionaryes for __slots__.

# Slots are class variables that can be assigned a string, an iterable
# or a sequence of strings of the instance variable names.
# When using slots, you name an object's instance variable up front,
# losing the ability to add them dynamically.

# An object instance using slots does not have a built-in dictionary.
# As a result, more space is saved and accessing attributes is faster.


"""
class CharacterWithoutSlots:
    
    organization = "Slate Rock and Gravel Company"
    
    def __init__(self, name, location):
        self.name = name
        self.location = location


without_slots = CharacterWithoutSlots('Fred Flinstone', 'Bedrock')
print(without_slots.__dict__)
# Prints {'name': 'Fred Flinstone', 'location': 'Bedrock'}
"""


# Implementing the above class using __slots__
class CharacterWithoutSlots:
    
    __slots__ = ["name", "location"]
    organization = "Slate Rock and Gravel Company"
    
    def __init__(self, name, location):
        self.name = name
        self.location = location
        
        
with_slots = CharacterWithoutSlots('Fred Flinstone', 'Bedrock')
# print(with_slots.__dict__)
# The above prints AttributeError: 'CharacterWithoutSlots'
# object has no attribute '__dict__'.
print(with_slots.name) # Prints 'Fred Flinstone'
print(with_slots.location) # Prints 'Bedrock'
print(with_slots.organization) # Slate Rock and Gravel Company


# Caveats to be mindful of while using __slots__
# 1. Trying to set an attribute
# that is not present in slots raises Attribute Error.

# with_slots.pet = "dino"
# AttributeError: 'character_with_slots' object has no attribute 'pet'.

# 2. Sub-classes will not follow the __slots__ assignement in superclass.
# This can be averted by declaring the __slots__
# variable once again in subclass.

# __slots__ can boost performance and optimize the code
# in making it more memory efficient.
