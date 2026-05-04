from ipaddress import ip_network

net = ip_network(r'68.203.243.87/255.255.224.0', 0)
for ip in net:
    print(ip, sum(list(map(int, f'{ip}'.split('.')))))