"""
Python: Pytest
        Learning Pytest with examples
        Greeting Example
"""

from pytest_greet import greet as hi
import pytest


@pytest.fixture
def bob():
    return {"name": "Bob"}


def test_hello(bob):
    assert hi(bob) == "Hi Bob"
