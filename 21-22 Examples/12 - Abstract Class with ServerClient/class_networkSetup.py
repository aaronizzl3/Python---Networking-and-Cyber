from abc import ABC, abstractmethod


class Network_Setup(ABC):
    def configuration(self, address, port):
        self.address = address
        self.port = port

    @abstractmethod
    def run(self):
        pass