
# TODO: FOR Loop - count from 0 through to 10.
for x in range(11):
    print(x)

# TODO: WHILE Loop - create a count which prints out 0 through to 10
counter = 0

while counter <= 10:
    print(counter)
    counter += 1

# TODO: Input, print out the number multiplied by 2, repeat this four times.
myNumber = int(input("Enter a number: "))

for x in range(4):
    myNumber *= 2
    print(myNumber)

# TODO: Extension task. Store the number 7. So long as it is greater than 7, print it out. Decrement each loop.
ourNumber = 7

while ourNumber > 0:
    print(ourNumber)
    ourNumber -= 1
