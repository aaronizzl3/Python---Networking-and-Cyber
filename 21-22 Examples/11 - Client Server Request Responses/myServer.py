# Import Libraries
import socket


# Create Socket Object
def create_socket():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    address = "127.0.0.1"
    port = 10123
    s.bind((address, port))
    return s


# Call Function
mySocket = create_socket()

# Run Socket
mySocket.listen(2)

while True:
    address, port = mySocket.accept()
    print(f"Connection received from: {address}")

    while True:
        try:
            data = address.recv(256)
            decoded = data.decode('utf-8')
            print(f"Received Request: {decoded}")
            if str(decoded) == "1":
                print("Some action. Continuing connection.")
            elif str(decoded) == "2":
                print("Client exiting.")
                break
        except socket.error as error:
            print(f"Error: {error}")

