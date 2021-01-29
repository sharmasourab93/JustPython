"""
Python: Pytest
        Learning Pytest with Example
        Fixtures in  Pytest
        Fixtures are used to replace
"""


import pytest


# Setting up the Fixture for use in Test functions
@pytest.fixture
def numbers():
    a, b, c = 10, 20, 25
    
    return [a, b, c]


# Setting Xfail
@pytest.mark.xfail
def test_method1(numbers):
    x = 15
    
    assert numbers[0] == x
    

# Setting Pytest to Skip
@pytest.mark.skip
def test_method2(numbers):
    y = 20
    assert numbers[1] == y
    

def test_method3(numbers):
    z = 25
    assert numbers[2] == z
