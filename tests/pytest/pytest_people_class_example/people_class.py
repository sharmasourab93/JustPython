"""
Python: Pytest
        Learning Pytest with Examples
        Class Person consumed by test_people_class
"""


class Person:
    
    def __init__(self, name, favorite_animal=None):
        self.name = name
        self.favorite_animal = favorite_animal
        

def anyone_like_dogs(people):
    """Check if 1 person likes dogs"""
    return any(
        [p.favorite_animal == "dog" for p in people]
        )
