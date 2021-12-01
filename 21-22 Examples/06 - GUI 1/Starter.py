"""Doc String, explaining the purpose of this specific file."""

# Imports


# Class Definitions
class MealCalculator:
    # Fields
    students = 0

    # Constructor
    def __init__(self, students):
        self.students = students
        self.MealSplit()

    # Methods
    def MealSplit(self):
        standard = int(input("How many students will be having standard meals?"))
        luxury = self.students - standard
        self.CalculatePrice(standard, luxury)

    def CalculatePrice(self, standard, luxury):
        standardPrice = standard * 2
        luxuryPrice = luxury * 3
        self.OutputPrice(standardPrice, luxuryPrice)

    def OutputPrice(self, standardPrice, luxuryPrice):
        print(f"Standard Cost: £{standardPrice}\n"
              f"Luxury Cost: £{luxuryPrice}\n"
              f"Overall (with VAT): £{(standardPrice + luxuryPrice) * 1.2}")


# Main Logic
MyObject = MealCalculator(20)

