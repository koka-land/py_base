from ipaddress import *

ans = 10**10

for mask in range(32, 15, -1):
    net1 = ip_network(f'157.220.185.237/{mask}', 0)
    net2 = ip_network(f'157.220.184.230/{mask}', 0)
    if net1 == net2:
        c1 = 0
        for ip in net1:
            if f'{ip:b}'.count('1') == 15:
                c1 += 1
        ans = min(ans, c1)

print(ans)