"""
Python: Pytest
        Learning Pytest with Examples
        Simple Pytest Program to test a function.
"""


import pytest


def func(x):
    """A Simple Function to return an argument + 5."""
    return x + 5


def test_method():
    """Simple test Function to assert the method to be tested."""
    assert func(3) == 8
    assert func(5) != 8
