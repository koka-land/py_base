from ipaddress import *

net = ip_network('172.16.168.0/255.255.248.0', 0)
c = 0

for i in net:
    if f'{i:b}'.count('1') % 5 != 0:
        c += 1

print(c)