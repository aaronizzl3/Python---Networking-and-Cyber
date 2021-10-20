# Import library to use abstract classes
from abc import ABC, abstractmethod


# Class with Abstract Method
class Polygon(ABC):
    def noofsides(self):
        pass


# Class with Overriding Abstract Method
class Triangle(Polygon):
    def noofsides(self):
        print("I have 3 sides!")


class Pentagon(Polygon):
    def noofsides(self):
        print("I have 5 sides!")


# Object Code
R = Triangle()
R.noofsides()

R = Pentagon()
R.noofsides()

