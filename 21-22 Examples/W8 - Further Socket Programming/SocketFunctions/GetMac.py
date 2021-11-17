# OS Independent getMacAddress() returns the mac address for any network adapter
# using OS specific methods depending on what sys.platform resolves to.
# No special usage.
import sys
import os


def get_mac_address():
    if sys.platform == 'win32':
        for line in os.popen("ipconfig /all"):
            if line.lstrip().startswith('Physical Address'):
                mac = line.split(':')[1].strip().replace('-',':')
                break
    else:
        for line in os.popen("/sbin/ifconfig"):
            if line.find('Ether') > -1:
                mac = line.split()[4]
                break
    return mac


mac_address = get_mac_address()
print ("Mac Address: %s" % mac_address)
