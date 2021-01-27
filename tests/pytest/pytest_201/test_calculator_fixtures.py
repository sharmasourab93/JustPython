"""
Python: Pytest
        Pytest 201
        test_calculator_fixtures consuming conftest
        Testing several features like
            1. Capsys
            2. Captured Print
            3. Monkey Patching
"""


import pytest
import calculator
from calculator import read_json
from conftest import my_fixture, captured_print


def test_my_fixture(my_fixture):
    assert my_fixture == 42


def test_capsys(capsys):
    print("hello")
    print("bye")
    out, err = capsys.readouterr()
    assert 'hello\nbye\n' == out


# For Monkey patching
def test_monkeypath(monkeypatch):
    def fake_add(a, b):
        return 42
    
    monkeypatch.setattr(calculator, "add", fake_add)
    assert calculator.add(2, 3) == 42


def test_tmpdir(tmpdir):
    some_file = tmpdir.join('something.txt')
    some_file.write('{"hello": "world"}')
    result = read_json(str(some_file))
    assert result["hello"] == "world"


def test_fixture_with_fixtures(capsys, captured_print):
    print("more")
    out, err = capsys.readouterr()
    print(out)
    assert out == "Hello\nmore\n"
