
# Send a list of numbers into a function, print out the sum, largest, smallest
def generate():
    option = int(input("How many numbers would you like in the list?"))
    theList = []

    for x in range(option):
        addNum = int(input("Number: "))
        theList.append(addNum)

    return theList

1, 2, 3
def sum(myList):
    theSum = 0
    for x in myList:
        theSum += x
    return theSum


def largest(myList):
    theLargest = myList[0]

    for x in myList:
        if x > theLargest:
            theLargest = x
    return theLargest


def smallest(myList):
    theSmallest = myList[0]

    for x in myList:
        if x < theSmallest:
            theSmallest = x

    return theSmallest


myList = generate()

total = sum(myList)
large = largest(myList)
small = smallest(myList)

print(f"List: {myList}\nSum: {total}\nLargest: {large}\nSmallest: {small}")