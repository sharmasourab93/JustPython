"""
Python: Pytest
        Learning Pytest with Examples
        Greeting Example
"""


def greet(person):
    return "Hi {name}".format(**person)


def test_greet():
    bob = {"name": "Bob"} # Arrange
    greeting = greet(bob) # Act
    assert greeting == "Hi Bob" # Assert
