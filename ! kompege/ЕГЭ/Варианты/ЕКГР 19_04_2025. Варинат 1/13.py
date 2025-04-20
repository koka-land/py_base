from ipaddress import *

sp = []

network = ip_network('208.74.51.243/255.255.252.0', 0)

for ip in network:
    sp.append(ip)

print(sp[-2])