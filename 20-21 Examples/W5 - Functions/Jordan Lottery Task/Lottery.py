import random

lotterynumbers = []

for i in range (0,6):
    number = random.randint(1,20)
    while number in lotterynumbers:
        number = random.randint(1,20)

    lotterynumbers.append(number)

    lotterynumbers.sort()

userNumbers = []
for i in range (0,6):
    number = int(input("Please enter a number between 1 and 20 : "))
    while (number in userNumbers or number<1 or number>20):
        print("Invalid number, please enter a number between 1 and 20")
        number = int(input("Please enter a number between 1 and 20: "))
    userNumbers.append(number)

print("Today's lottery numbers are:")
print(lotterynumbers)

print("Your selection:")
print(userNumbers)