
# TODO: Print out the largest of three numbers.
a = 1
b = 2
c = 3

if a > b and a > c:
    largest = a
elif b > a and b > c:
    largest = b
elif c > a and c > b:
    largest = c
else:
    print("The numbers are equal.")

print(f"The largest number is {largest}")

# TODO: Input age and ask if eligible to vote.
myAge = int(input("What is your age? "))

if myAge >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# TODO: Determine whether a number is even or odd. nth term.
ourNumber = int(input("Enter a number: "))

if ourNumber % 2 == 0:
    print("You are even.")
else:
    print("You are odd.")








