"""
Python: Pytest
        Pytest 101
        Learning pytest with Examples
        Pytest for Calculator Class
"""


from calculator import Calculator, CalculatorError
import pytest


def test_add_weird_stuff():
    """Test Function to test Calculator's add method
       having arguments other than int.
    """
    
    # Arrange
    calculator = Calculator()
    
    # Act
    # Use with context to raise
    with pytest.raises(CalculatorError) as context:
        result = calculator.add("two", "three")
    
    # Assert
    # assert result == 5
    assert str(context.value) == 'Wrong'
    

def test_subtract():
    """Test Function to test subtract method of Calculator Class."""
    # Arrange
    calculator = Calculator()
    # Act
    result = calculator.subtract(3, 2)
    # Assert
    assert result == 1
    

def test_multiply():
    # Arrange
    calculator = Calculator()
    # Act
    result = calculator.multiply(3, 2)
    # Assert
    assert result == 6
