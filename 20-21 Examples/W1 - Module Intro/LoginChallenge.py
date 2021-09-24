
# TODO: You have been tasked with creating a login system.

# TODO: The system should do the following:

# TODO: Take input for username and password

# TODO: Check the username and password match "Admin" and "Password12"

# TODO: Print out "Access granted" or "Access Denied" based on the result.

username = input("Enter username: ")
password = input("Enter password: ")

if username == "Admin":
    print("Username correct.")
    if password == "Password12":
        print("Both entries correct, logged in.")
    else:
        print("Password incorrect.")
else:
    print("Username incorrect.")