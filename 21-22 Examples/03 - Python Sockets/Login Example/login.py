import csv


def read_data():
    data = []
    # open and read data from csv file
    # if we wanted a dictionary we could use csv.DictReader(FILE, DELIMITER)
    with open('users.csv') as csv_file:
        read_csv = csv.reader(csv_file, delimiter=',')
        # read and store data
        for row in read_csv:
            data.append(row)
    # return list of elements
    return data


def check_login(username, password, users):
    # cycle through rows to find username and password match
    for row in users:
        # check for match
        if username == row[1] and password == row[2]:
            # return true if match is found
            return row
    # return false if no match is found
    return False


def login(username, password, user_data):
    # call check_login function to validate
    check = check_login(username, password, user_data)
    # if check_login returns False:
    if not check:
        print("Invalid Login!")
    # if check_login does not return False:
    else:
        print("Welcome,", check[4])
        print("You are logged in as an", check[3], "User")


def main():
    # request username and password
    username = input("Please enter Username: ")
    password = input("Please enter Password: ")
    # call login function with user input + read_data() return
    login(username, password, read_data())


main()
