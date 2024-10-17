from ipaddress import *

network = ip_network('172.16.168.0/255.255.248.0')
print(network)
ans = 0

for ip in network:
    x = f'{ip:b}'
    if x.count('1') % 5 != 0:
        ans += 1
        
print(ans)
