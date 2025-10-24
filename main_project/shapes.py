import math
from abc import abstractmethod, ABC

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    
    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
class Rectangle(Shape):

    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def __eq__(self, other) -> bool:
        if not isinstance(other, Rectangle):
            return False
        return self.length == other.length and self.width == other.width
    
    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length * 2) + (self.width * 2)

    