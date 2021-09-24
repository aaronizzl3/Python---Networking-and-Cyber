
# TODO: Create two variables which hold 4 and 7. Prove which one is largest.
numA = 4
numB = 7

if numA > numB:
    print(str(numA) + " is the largest number.")
elif numA == numB:
    print(str(numA) + " is equal to " + str(numB))
else:
    print(str(numB) + " is the largest number.")

# TODO: Store the name Student. Create an IF which shows they're an admin, student or unauthorised.
role = "Student"

if role == "Admin":
    print("You are an admin.")
elif role == "Student":
    print("You are a student.")
else:
    print("You are unauthorised.")

# TODO: Create an IF statement that checks if a user likes apples and is older than twenty one.
likesApples = input("Do you like apples? Y/N")
askAge = int(input("How old are you? "))

if likesApples == "Y" and askAge >= 21:
    print("The user likes apples and is older than or equal to 21.")
elif likesApples == "Y" and askAge < 21:
    print("The user likes apples and is not older than 21.")
elif likesApples == "N" and askAge >= 21:
    print("The user does not like apples and is older than or equal to 21.")
else:
    print("The user does not like apples and is not older than 21.")
