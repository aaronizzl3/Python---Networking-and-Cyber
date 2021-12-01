# Global Variables
tickets = []

# Class Definitions
class User:
    name = ""
    jobTitle = ""

    def __init__(self, name, jobTitle):
        self.name = name
        self.jobTitle = jobTitle

    def ChangeDetails(self):
        option = input("Enter new job title: ")
        self.jobTitle = option

    def AddTicket(self):
        addTicket = input("Enter ticket number: ")
        tickets.append(addTicket)


class Support(User):

    def __init__(self, name):
        User.__init__(self, name, "First Line Support")

    def RemoveTicket(self):
        removeTicket = input("Enter ticket number: ")

        try:
            tickets.remove(removeTicket)
            print("Ticket removed.")
        except:
            print("Ticket doesn't exist.")



# Main Logic
myUser = User("Aaron", "Lecturer")
myUser.AddTicket()
mySupport = Support("Sang-woo")
mySupport.RemoveTicket()
print(tickets)