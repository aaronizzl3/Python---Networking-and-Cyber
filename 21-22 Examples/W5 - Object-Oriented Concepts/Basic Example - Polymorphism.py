
# Polymorphism - using the same function or class, but for different types of use

# Inbuilt Polymorphic Functions
print(len("geeks"))
print(len([10, 20, 30]))


# Polymorphism with Class Methods
class India():
    def capital(self):
        print("New Delhi")

    def language(self):
        print("Hindi")

    def type(self):
        print("Developing Country")


class USA():
    def capital(self):
        print("Washington DC")

    def language(self):
        print("English")

    def type(self):
        print("Developed Country")


# Objects
obj_ind = India()
obj_usa = USA()

# We call the methods without being concerned about which class type each object is, and assume they exist in each class
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
    country.type()

# Bare in mind, this may be the concept you are least likely to use in your program
