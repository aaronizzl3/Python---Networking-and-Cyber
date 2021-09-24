# TODO: Take input from the user for the forename and surname.
fName = input("Enter your forename: ")
sName = input("Enter your surname: ")

# TODO: Print out the full name in the format "Forename Surname"
# Concatenation
print(fName + " " + sName)
# Printing values one after the other
print(fName, sName)
# Formatted String
print(f"{fName} {sName}")
# Parameter String
print("%s %s" % (fName, sName))

# TODO: RECAP Variables Data Types Operators
myVariable = "Data"
myString = "String 123"
myInteger = 42
myBoolean = True
myFloat = 4.4

# Operators + - / * % > < == += -=
numA = 1
numB = 2
print(numA + numB)
print(numA > numB)
