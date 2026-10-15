import re

def validate_ip(ip):
    # IPv4
    ipv4 = r'^(\d{1,3}\.){3}\d{1,3}$'

    # IPv6
    ipv6 = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'

    if re.match(ipv4, ip) or re.match(ipv6, ip):
        return True
    return False


ip = input("Enter IP address: ")
if validate_ip(ip):
    print("True - Valid IP address")
else:
    print("False - Invalid IP address")