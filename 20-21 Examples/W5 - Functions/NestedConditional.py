

username = input("Enter a username: ")
password = input("Enter a password: ")

if username == "Admin":
    if password == "Password":
        print("Authorised.")
    else:
        print("Password incorrect.")
else:
    print("Username incorrect.")
