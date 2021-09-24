
# TODO: Import Module
import random

# TODO: Generate random number
myNumber = random.randint(1, 3)

# TODO: Guess the number
guess = int(input("Guess the number: "))

if guess == myNumber:
    print("You guessed correct!")
else:
    print("You guessed WRONG fool!")

print(myNumber)
