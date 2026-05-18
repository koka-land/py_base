from ipaddress import ip_network

net = ip_network(f'115.192.0.0/255.192.0.0', 0)
ans = 0

for ip in net:
    if f'{ip:b}'.count('1') % 3 != 0:
        ans += 1
print(ans)