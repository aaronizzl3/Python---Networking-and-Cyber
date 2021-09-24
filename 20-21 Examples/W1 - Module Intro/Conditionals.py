
# TODO: IF/ELIF/ELSE
temperature = int(input("What is the temperature? "))

if temperature > 20:
    print("It's warm.")
elif temperature > 0:
    print("It's cold.")
else:
    print("It's freezing!")

# NEW
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if name == "Aaron" or age == 27:
    print("At least one credential correct.")
else:
    print("Credentials incorrect.")
