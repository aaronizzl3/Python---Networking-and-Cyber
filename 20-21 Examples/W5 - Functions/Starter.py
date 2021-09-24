
# TODO: Create an application which uses a list. Tell us how many numbers are larger than five and which they are.

myList = [7, 12, 5, 3, 5, 10, 15, 18, 22, 1, 4]
total = 0

for number in myList:
    if number > 5:
        print(f"{number} is greater than five.")
        total += 1

print(f"There are {len(myList)} items in the list.")
print(f"{total} numbers are larger than five.")


# TODO: Utilise a loop, allow the user to append five numbers of their choice to a list.

theList = []

for x in range(5):
    option = int(input("Enter a number: "))
    theList.append(option)

print(theList)

