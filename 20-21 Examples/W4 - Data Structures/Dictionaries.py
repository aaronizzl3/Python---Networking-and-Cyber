

# Initialise a dictionary
myDictionary = {
    "Name": "Aaron Hussain",
    "Role": "Lecturer",
    "Specialty": "Programming and Web"
}

# Access a value
print(myDictionary.get("Specialty"))

# Change a value
myDictionary["Role"] = "Programme Leader"
print(myDictionary)

# Add a value
myDictionary["Hobby"] = "eSports, Running, Chess"
print(myDictionary)

# Remove a value
myDictionary.pop("Specialty")
print(myDictionary)

# Empty a dictionary
myDictionary.clear()

# LOADED QUESTION
myList = [1, 2, 3]
myList2 = [4, 5, 6]

dictionary = {
    "List1": myList,
    "List2": myList2
}

print(dictionary)