# Import Libraries
import socket
from class_networkSetup import Network_Setup


class Server(Network_Setup):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __init__(self, address, port):
        self.configuration(address, port)

    def run(self):
        self.s.bind((self.address, self.port))
        self.s.listen(2)

        while True:
            address, port = self.s.accept()
            print(f"Connection received from: {address}")

            while True:
                try:
                    data = address.recv(256)
                    decoded = data.decode('utf-8')
                    print(f"Received Request Code: {decoded}")
                    if str(decoded) == "1":
                        ipData = address.recv(256)
                        decodedIP = ipData.decode('utf-8')
                        print(f"IP Received: {decodedIP}")
                    elif str(decoded) == "2":
                        print("MAC Received: ")
                    elif str(decoded) == "3":
                        print("Client exiting.")
                        break
                except socket.error as error:
                    print(f"Error: {error}")


myObject = Server("127.0.0.1", 10150)
myObject.run()
