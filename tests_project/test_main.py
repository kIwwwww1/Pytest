import pytest
from main_project.main import add, divide

def test_add():
    assert 5 == add(4, 1)

def test_divide():
    assert divide(15, 3) == 5