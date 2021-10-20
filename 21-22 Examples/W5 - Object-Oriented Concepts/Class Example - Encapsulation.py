
class Student:
    __name = ""

    def __init__(self, name):
        self.__name = name

    def SayHello(self):
        print(f"Hello {self.__name}!")

    # Getters and Setters
    def set_name(self, newName):
        newName += " SquidGame"
        self.__name = newName

    def get_name(self):
        return self.__name


myObject = Student("Aaron")
myObject.set_name("Sang-woo")
myObject.SayHello()

ourName = myObject.get_name()
print(ourName)