"""
Python: Pytest
        Learning Pytest with Examples
        Grouping in Pytest
        Using Class as a Wrapper for Grouping.
"""


class TestClass:
    """ TestClass Serving as wrapper for Test Methods. """
    def test_one(self):
        x = 'edureka'
        assert 'r' in x
    
    def test_two(self):
        x = 'hello'
        assert hasattr(x, 'check')
