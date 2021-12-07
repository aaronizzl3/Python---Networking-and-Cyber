import socket


class Database_Handler:
    db_address = None

    def get_ip_address(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip

    def set_address(self):
        ip_address = self.get_ip_address()
        self.db_address = ip_address


myObject = Database_Handler()
myObject.set_address()
print(f"IP Address: {myObject.db_address}")