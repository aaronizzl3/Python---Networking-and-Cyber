# Port scanner example code for CMP203 Cyber Security Programming
# No special usage.

import socket
import sys

# The example will scan the localhost (127.0.0.1) - obviously this isn't great
# Scanning the localhost of a PC/Server won't always give a true picture of how your machine looks on the outside
remoteServer = "127.0.0.1"
remoteServerIP = socket.gethostbyname(remoteServer)

print("Please wait, scanning remote host", remoteServerIP)

# Use the range function to specify portscan range
# This will take some time.. so you need to wait
# Example will scan 1 to 1024
try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print("Port {}: 	 Open".format(port))
        sock.close()

# If this doesn't work CTRL + F2 will stop PyCharm (or the little stop button in the bottom left)
except KeyboardInterrupt:
    print("You pressed Ctrl+C")
    sys.exit()

# GAI = Get Address Info (getaddrinfo()) and gives errors specific to the remote host
except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

# General socket errors
except socket.error:
    print("Couldn't connect to server")
    sys.exit()
