
# Imports
from datetime import date

# Main Program
for x in range(3):
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    if username == "Admin" and password == "Password":
        print("Access granted.")
        menu = True
        break
    else:
        print("Access denied.")
        menu = False

while menu:
    print("1 - Date\n2 - Exit")
    option = input("Option: ")

    if option == "1":
        print("Date: ", date.today())
    elif option == "2":
        print("Exiting.")
        break
    else:
        print("Invalid input.")


