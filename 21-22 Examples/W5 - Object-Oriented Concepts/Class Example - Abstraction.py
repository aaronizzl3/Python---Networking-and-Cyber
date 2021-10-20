# Imports
from abc import ABC, abstractmethod

# Global Variables


# Abstract Class
class Shape(ABC):
    @abstractmethod
    def CalculateArea(self):
        pass

    def NumSides(self, sides):
        print(f"You have {sides} number of sides.")


class Square(Shape):
    def CalculateArea(self):
        print("Width x Length")


class Triangle(Shape):
    def CalculateArea(self):
        print("Height x Base / 2")


class Pentagon(Shape):
    pass


myObject = Square()
myObject.CalculateArea()

secondObject = Triangle()
secondObject.CalculateArea()

thirdObject = Pentagon()
thirdObject.CalculateArea()

