from abc import ABC, abstractmethod


class Network_Functionality(ABC):
    host = None
    port = None

    def conf_socket(self):
        pass

    def send_message(self):
        pass

    def recv_message(self):
        pass


class Server(Network_Functionality):
    pass


class Client(Network_Functionality):
    pass
