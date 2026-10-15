import re

def validate_ip(ip):
    ipv4 = r'^(\d{1,3}\.){3}\d{1,3}$'
    ipv6 = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'

    if re.match(ipv4, ip):
        parts = ip.split(".")
        return all(0 <= int(part) <= 255 for part in parts)

    if re.match(ipv6, ip):
        return True

    return False


ip = input("Enter IP address: ")

print("Valid IP address." if validate_ip(ip) else "Invalid IP address.")