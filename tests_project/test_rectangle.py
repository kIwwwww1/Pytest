import pytest
from main_project.shapes import Rectangle

@pytest.fixture()
def my_rectangle():
    return Rectangle(10, 20)

@pytest.fixture()
def fake_rectangle():
    return Rectangle(5, 6)

def test_area(my_rectangle):
    assert my_rectangle.area() == 10 * 20

def test_perimeter(my_rectangle):
    assert my_rectangle.perimeter() == (10 * 2) + (20 * 2)

def test_not_eq_(my_rectangle, fake_rectangle):
    assert my_rectangle != fake_rectangle