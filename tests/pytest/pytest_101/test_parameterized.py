"""
Python: Pytest
        Learning Pytest with Examples
        Learning to Pass Multiple Parameters and testing the method
"""


import pytest


@pytest.mark.parametrize("x, y, z",
                         [(10, 20, 200),
                          (20, 40, 600)])
def test_method(x, y, z):
    assert x * y == z
