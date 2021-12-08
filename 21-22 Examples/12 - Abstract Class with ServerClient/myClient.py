# Import Libraries
import socket
from time import sleep
from class_networkSetup import Network_Setup


class Client(Network_Setup):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, address, port):
        self.configuration(address, port)


    def get_ip_address(self):
        ip = self.s.getsockname()[0]
        return ip

    def run(self):
        self.s.connect((self.address, self.port))
        print("Connection established.")

        while True:
            try:
                print("1 - Send IP \n2 - Send MAC\n3 - Exit")
                message = input("Request ID: ")
                encodedMessage = message.encode()
                self.s.sendall(encodedMessage)
                if int(message) == 1:
                    sleep(1)
                    encodedMessage = self.get_ip_address().encode()
                    print(encodedMessage)
                    self.s.sendall(encodedMessage)
                if int(message) == 2:
                    pass
                if int(message) == 3:
                    break
            except socket.error as error:
                print(f"Error: {error}")


myObject = Client("127.0.0.1", 10150)
myObject.run()