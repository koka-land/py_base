from ipaddress import *

for mask in range(24, 15, -1):
    net = ip_network(f'127.63.67.1/{mask}', 0)
    f = 0
    for ip in net:
        if f'{ip:b}'[:16].count('1') < f'{ip:b}'[16:].count('1'):
            f = 1
            break
    if f == 0:
        print(int('1' * (mask - 16) + '0' * (8 - (mask - 16)), 2))