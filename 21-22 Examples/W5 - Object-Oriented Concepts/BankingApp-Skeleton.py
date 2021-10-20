# Imports
from abc import ABC, abstractmethod

# Global Variables


# Class Definitions
class Account(ABC):
    def deposit(self):
        pass

    def withdraw(self):
        pass

    @abstractmethod
    def check_balance(self):
        pass


class SavingsAccount(Account):
    balance = None

    def __init__(self):
        pass


class CurrentAccount(Account):
    balance = None

    def __init__(self):
        pass


# Main Logic
myObject = SavingsAccount()
