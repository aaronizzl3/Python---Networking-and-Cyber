

# Base Class
class Base:
    def __init__(self):
        # We prefix the variable name with an underscore (_) in order to show it is a protected member
        self._a = 2


#Derived Class
class Derived(Base):
    def __init__(self):
        # Call the CONSTRUCTOR of the base class
        Base.__init__(self)
        print("Calling protected member of base class")
        print(self._a)


# Called protected member outside of the class will cause an error
obj1 = Base()
print(obj1.a)

# Remove the line above and only use the second - the derived class will work, but we can't access anything in the base class
obj2 = Derived()


