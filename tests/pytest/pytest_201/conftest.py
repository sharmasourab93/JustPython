"""
Python: Pytest
        Pytest 201
        Conftest consumed by test_fixtures
"""


import pytest


@pytest.fixture
def my_fixture():
    return 42


@pytest.fixture
def captured_print(capsys):
    print("Hello")
