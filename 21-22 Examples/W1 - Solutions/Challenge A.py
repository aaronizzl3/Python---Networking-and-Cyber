# Create a menu which takes two numbers, and lets the user choose a Maths operation

def menu():
    A = int(input("Enter your first number: "))
    B = int(input("Enter your second number: "))

    option = int(input("MENU\n"
                       "1 - Addition\n"
                       "2 - Subtraction\n"
                       "Option: "))

    if option == 1:
        addition(A, B)
    elif option == 2:
        subtraction(A, B)
    else:
        print("Invalid input.")


def addition(numberA, numberB):
    print(f"{numberA} + {numberB} = {numberA + numberB}")


def subtraction(numberA, numberB):
    print(f"{numberA} - {numberB} = {numberA - numberB}")


menu()