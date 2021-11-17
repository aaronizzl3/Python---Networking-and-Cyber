# OS Independent get_ip_address() returns the connected IP Address
# A socket connection is made to Google's public DNS to obtain the IP correct hostname
# This is because the socket.gethostbyname(socket.gethostname()) does not always return correct information
# For example, if the machine has a hostname set as "127.0.0.1" socket.gethostname() can return incorrect data

import socket


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


ip_address = get_ip_address()

print("IP Address: %s" % ip_address)
