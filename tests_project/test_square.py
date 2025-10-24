import pytest
from main_project.shapes import Square

@pytest.mark.parametrize('length, expected', [
    (2, 4),
    (4, 16),
    (9, 81)
])
def test_area_square(length, expected):
    assert Square(length=length).area() == expected

@pytest.mark.parametrize('length, expected', [
    (5, 20),
    (6, 24),
    (8, 32)
])
def test_perimeter_square(length, expected):
    assert Square(length=length).perimeter() == expected