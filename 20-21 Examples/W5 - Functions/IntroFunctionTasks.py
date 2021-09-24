
# TODO: 1 - Subtraction Function


def Subtraction():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(f"{a} - {b} = {a - b}")


Subtraction()

# TODO: 2 - Takes two numbers as arguments. Multiplies. Prints.


def Multiply(a, b):
    print(f"{a} * {b} = {a * b}")


Multiply(5, 2)

# TODO: 3 - Call a function, ask the user to input their name. Return it so it can be used outside.


def Name():
    yourName = input("Enter your name: ")
    return yourName


myString = Name()
print(f"{myString} is your name.")