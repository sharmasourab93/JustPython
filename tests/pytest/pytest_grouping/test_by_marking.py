"""
Python: Pytest
        Learning Pytest with Examples
        Pytest Grouping By Marking
"""


import pytest


# Marking Set as One
@pytest.mark.one
def test_method1():
    x = 5
    y = 10
    
    assert x == y
    

# Marking Set as two
@pytest.mark.two
def test_method2():
    a, b = 15, 20
    
    assert a + 5 == b


"""
On the command line,
The name one and two after mark
can be used in place of the test_method names.
This is called Grouping based on Markings.

# 1. $>pytest -k one -v pytest_by_marking.py
# 2. $>pytest -k two -v pytest_by_marking.py
"""
