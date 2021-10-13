
# Class Definition
class Dog:
    # Attributes
    Name = None
    Breed = None
    Colour = None

    # Class Constructor
    def __init__(self, Name, Breed, Colour="Blue"):
        self.Name = Name
        self.Breed = Breed
        self.Colour = Colour

    # Class Methods
    def bark(self):
        print("Woof!")

    def say_name(self):
        print(self.Name)


# Creating an Object
DogOne = Dog("Berty", "Chihuahua", "Ginger")
DogOne.say_name()
DogOne.bark()

# Second Object
DogTwo = Dog("Rex", "Toy Dinosaur", "Green")
DogTwo.say_name()

# Manipulating an Object
DogTwo.Name = "Big Rex"

# Third Object
DogThree = Dog("Wally", "Aliendog")
print(DogThree.Colour)





