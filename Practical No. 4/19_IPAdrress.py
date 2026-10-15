# 3.	Write a program to design a configuration system for a web server where some configuration settings should not be changed during runtime, while others can be updated. The server settings are as follows:
# ●	server_ip: A tuple representing the IP address of the server, which should remain unchanged.
# ●	allowed_ips: A list of IP addresses allowed to connect to the server, which can be updated during runtime.

# Web Server Configuration System

server_ip = (input("Enter server IP: "),)
allowed_ips = [input("Enter allowed IP: ")]

def update_configuration():
    new_ip = input("Enter IP to add: ")
    allowed_ips.append(new_ip)

    try:
        server_ip[0] = input("Enter new server IP: ")
    except TypeError:
        print("server_ip cannot be changed because it is a tuple.")


print("\nOriginal Configuration:")
print("Server IP:", server_ip)
print("Allowed IPs:", allowed_ips)

update_configuration()

print("\nUpdated Configuration:")
print("Server IP:", server_ip)
print("Allowed IPs:", allowed_ips)
