# Import Libraries
import socket


# Create Socket Object
def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return s


# Connect to Server
mySocket = create_socket()
mySocket.connect(("127.0.0.1", 10123))
print("Connection established.")

while True:
    try:
        print("1 - Continue\n2 - Exit")
        message = input("Request ID: ")
        encodedMessage = message.encode()
        mySocket.sendall(encodedMessage)
        if int(message) == 2:
            break
    except socket.error as error:
        print(f"Error: {error}")
