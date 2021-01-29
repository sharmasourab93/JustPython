"""
Python: Pytest
        Pytest 201
        test_calculator consuming calculator for testing
"""


import pytest
import calculator as calc
from calculator import add, MysteryError, subtract


class TestAdd:
    """ Class TestAdd is a Wrapper to all the below test methods. """
    
    def test_basics(self):
        assert True
        
    def test_add(self):
        assert add(1, 2) == 3
    
    def test_error(self):
        with pytest.raises(MysteryError):
            add(99, 1)
      
    # Parametrize
    @pytest.mark.parametrize('x, y, z', [(1, 1, 2),
                                         (2, 2, 4)
                                         ]
                             )
    def test_with_params(self, x, y, z):
        assert add(x, y) == z
