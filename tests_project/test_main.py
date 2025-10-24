import time
import pytest
from main_project.main import add, divide

@pytest.mark.skip(reason='Пока не работает!')
def test_skip():
    assert add(5, 4)

def test_add():
    assert 5 == add(4, 1)

def test_divide():
    assert divide(15, 3) == 5

@pytest.mark.slow
def test_very_slow():
    time.sleep(2.5)
    assert divide(15, 3) == 5

@pytest.mark.xfail(reason='Так нельзя')
def test_fail_divide():
    assert divide(4, 0)
