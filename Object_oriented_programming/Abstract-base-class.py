from abc import ABC, abstractmethod

class Shape(ABC):  # we can't make object using abstract base class
    @abstractmethod  # it order all its inhertet class to apply all function of it
    def print_area(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7

    def print_area(self):
        return self.length * self.breadth

tryobj = Shape() # it gives error

rect1 = Rectangle()
print(rect1.print_area())