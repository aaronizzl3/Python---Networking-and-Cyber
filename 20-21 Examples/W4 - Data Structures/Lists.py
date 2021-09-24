
# Initialising an empty list
myList = []

# Initialising a list with values
fruits = ["Apple", "Pear", "Plum", "Banana"]

# Access these values
print(fruits[0])

# Changing a Value
fruits[3] = "Kiwi"
print(fruits)

# Adding a Value
fruits.append("Mango")
print(fruits)

# Removing a Value
fruits.pop(1)
fruits.remove("Apple")
print(fruits)

# Looping through a list
for item in fruits:
    if item == "Mango":
        print("The mango exists.")
    else:
        print("No mango, no joy.")

# Check if item exists
if "Mango" in fruits:
    print("The mango STILL exists.")
else:
    print("The mango is dead.")