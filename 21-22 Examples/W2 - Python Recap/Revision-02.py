# Lists
myList = ["Apple", "Banana", "Plum"]
listNums = [4, 8, 9]

if 4 in listNums:
    print("True")

myList = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in myList:
    for col in row:
        print(col)

print(myList[0][0])

# Dictionaries
myDict = {
    "Fruit": "Apple",
    "Age": 5,
    1993: "DOB"
}

# Modifies
myDict["Fruit"] = "Banana"

# Appends
myDict["SomethingNew"] = "Blah"

# Accesses
print(myDict.get("Fruit"))

# Example of Use of Dict
myBlog = {
    "Title": "TitleofPost",
    "Date": "DateofPost",
    "Content": "Content",
    "Author": "AuthorsNameHere"
}

# Data Structures within Data Structures
myDictionary = {
    "Logic": [1, 2]
}

# Accessing Dictionary
myData = myDictionary.get("Logic")
print(myData[0])

# Functions
myShoppingList = []


def AddItem(myList):
    toAdd = input("What would you like to add?").lower()
    myList.append(toAdd)
    return myList


def RemoveItem(myList):
    toRemove = input("What would you like to remove?").lower()

    if toRemove in myList:
        myList.remove(toRemove)

    return myList

myShoppingList = AddItem(myShoppingList)
for x in myShoppingList:
    print(x.capitalize())
myShoppingList = RemoveItem(myShoppingList)
print(myShoppingList)


# Loops
x = 0
name = "Aaron"


while True:
    print("Hello")

    x += 1

    if x < 10:
        continue
    else:
        break

# Logical Operators
# TODO: AND, OR, NOT
breakfast = "Cereal"

if name == "Aaron" and breakfast == "Banana" or breakfast == "Cereal":
    pass

if name == "Aaron":
    if breakfast == "Banana" or breakfast == "Cereal":
        pass