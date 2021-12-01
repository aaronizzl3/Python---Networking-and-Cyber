# Globals
accounts = [
    ["Lemon", "password12"],
    ["Aaron", "qwerty123"],
    ["Admin", "Poophead"]
]

# User Class
class User:
    username = ""
    auth = None

    # Constructor
    def __init__(self, username):
        self.username = username
        self.auth = True

# Menu Class
class Menu:
    user = None

    def __init__(self, user):
        self.user = user
        print("1 - Say Hello\n2 - Say Goodbye")
        option = int(input("Option: "))

        if option == 1:
            self.optionOne()
        elif option == 2:
            self.optionTwo()
        else:
            print("Bad input.")

    # Class Methods
    def optionOne(self):
        print(f"Hello {self.user.username}")

    def optionTwo(self):
        print("Say Goodbye!")


# Main Logic
username = input("Enter username: ")
password = input("Enter password: ")

for i in accounts:
    if i[0] == username and i[1] == password:
        print("Logged in")
        myUser = User(i[0])
        running = Menu(myUser)
        break