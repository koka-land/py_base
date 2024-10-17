from ipaddress import *

network = ip_network(f'228.172.224.0/255.255.240.0', 0)
ans = 0

for ip in network:
    x = f'{ip:b}'
    if x.count('1') % 5 != 0:
        ans += 1

print(ans)

ans = 0
for i in range(2 ** 12):
    if ((bin(i)).count('1') + 11) % 5 != 0:
        ans += 1

print(ans)