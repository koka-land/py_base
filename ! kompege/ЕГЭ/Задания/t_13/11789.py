from ipaddress import *

for mask in range(16, 25):
    net = ip_network(f'99.8.254.232/{mask}', 0)
    f = 0
    for ip in net:
        if f'{ip:b}'[:16].count('1') > f'{ip:b}'[16:].count('1'):
            f = 1
            break
    if f == 0:
        print(str(net.netmask).split('.')[2])
        break
