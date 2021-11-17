# OS Independent get_computer_name prints Computer name
# This demonstrates 3 possible methods of doing this.
# No special usage.

import platform
import socket
import os


def get_computer_name():
    # Method 1
    print(platform.node())
    # Method 2
    print(socket.gethostname())
    # Method 3
    print(os.environ['COMPUTERNAME'])


get_computer_name()
