"""
Python: Pytest
        Learning Pytest with examples
        Pytest module for testing dnd.py and objects in it.
"""


from dnd import attack_damage
from unittest import mock


# Fix Return Value & Set AutoSpec in Pytest
@mock.patch('dnd.randint', return_value=10)
def test_attack_damage(mock_randint):
    """Mocked Test Function."""
    assert attack_damage(6) == 16
    mock_randint.assert_called_once_with(1, 8)
