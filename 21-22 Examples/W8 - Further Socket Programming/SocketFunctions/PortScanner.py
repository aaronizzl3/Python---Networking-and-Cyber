# Imports
import socket
import subprocess  # PS
import sys
import time
from datetime import datetime  # PS

# Class - Create Socket / Start Program
class SysScan:
    # Console Frame
    def frame(self):
        print("-" * 60)


    # Creation of Socket
    def runtest(self):
        fail = "Failed to create socket."
        success = "Socket created."
        startup = "Program startup."
        name = input("Enter username: ")
        try:
            print("Welcome " + name + ".")
            print(startup)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print(success)
        except socket.error:
            sys.exit
            print(fail)


    # Initial Test / Ready
    def initialtest(self):
        testhost = "www.google.com"
        unresolved = "Hostname could not be resolved. Exiting."
        resolved = "Test successful. Program is ready for operation."
        try:
            remote_ip = socket.gethostbyname(testhost)
            print("Test Address: " + testhost + " / " + remote_ip)
            print(resolved)
        except socket.gaierror:
            sys.exit(unresolved)


    def localscan(self):
        remoteserver = input("Enter a remote host to scan: ")
        print("Please wait, the tool is scanning the remote host.")
        self.frame()
        remoteserverip = socket.gethostbyname(remoteserver)
        try:
            for port in range(1, 1025):  # 1025
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                result = sock.connect_ex((remoteserverip, port))
                if result == 0:
                    print(time.strftime("%H:%M:%S - ") + "Port {}: Open".format(port))
                sock.close()
        except KeyboardInterrupt:
            sys.exit("Error: You pressed Ctrl + C.")

        except socket.gaierror:
            sys.exit("Error: Hostname could not be resolved.")

        except socket.error:
            sys.exit("Error: Couldn't connect to the server.")

        print("Scan finished.")
        self.frame()


# TESTING CODE
def program():
    scanA = SysScan()
    scanA.frame()
    scanA.runtest()
    scanA.initialtest()
    scanA.frame()
    scanA.localscan()

program()
