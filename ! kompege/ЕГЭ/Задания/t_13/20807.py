from ipaddress import *

net = ip_network(f'172.16.192.0/255.255.192.0', 0)
ans = 0

for ip in net:
    if f'{ip:b}'.count('1') % 5 != 0:
        ans += 1

print(ans)