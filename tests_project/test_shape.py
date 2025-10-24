import math
import pytest
from sympy import Circle
from main_project.shapes import Circle

class TestCircle():

    def setup_method(self, method):
        print(f'Подняли настройки {method}')
        self.circle = Circle(10)

    def teardown_method(self, method):
        print(f'Отключили настройки {method}')

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2
    
    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius