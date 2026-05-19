from ipaddress import *
net = ip_network('192.168.108.157/255.255.255.192', 0)
n = 0
for ip in net:
    print(n, ip)
    n += 1