"""
Python: Pytest
        Learning Pytest with Examples
        Pytest - testing objects from people class
"""

from people_class import Person, anyone_like_dogs
import pytest


@pytest.fixture
def person(**kwargs):
    count = 0
    
    def _person(**kwargs):
        nonlocal count
        count += 1
        name = kwargs.pop("name", f"Bob {count}")
        return Person(name=name, **kwargs)
    
    return _person


def test_anyone_like_dogs_true(person):
    people = [person(favorite_animal="cat"),
              person(favorite_animal="dog")
              ]
    assert anyone_like_dogs(people) is True


def test_person(person):
    assert person().name != person().name
    assert person(name="Alice").name == "Alice"
