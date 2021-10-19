
# Original Class - this is what will inherited by our next class
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side " +str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side", i+1, "is", self.sides[i])


# Example of using an object from our original
ourShape = Polygon(4)
ourShape.inputSides()
ourShape.dispSides()


# Class using Inheritance
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        # Calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print("The area of the triangle is %0.2f" %area)


# Example of using our new object
print("\n")
newShape = Triangle()
newShape.inputSides()
newShape.findArea()


