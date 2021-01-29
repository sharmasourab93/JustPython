"""
Python: Pytest
        Learning Pytest with Examples
        Pytest Grouping By Substring Matching
"""


import pytest


def test_method1():
    x = 5
    y = 10
    
    assert x == y


def test_method2():
    a, b = 15, 20
    
    assert a + 5 == b


"""
On the command line,
Functions carrying string test are
tested and set on or off based on the selected substring.

# 1. $>py.test -k method1 -v filename.py
(1) would only run method 1

# 2. $>py.test -k method2 -v filename.py
(2) would only run method 2
"""
