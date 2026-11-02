from ipaddress import ip_network
ans = 0
for a in range(255, -1, -1):
    u = f'116.242.{str(a)}.26/255.255.255.224'
    network = ip_network(u, 0)
    fl = 0
    for ip in network:
        ak = list(map(int, str(ip).split('.')))
        if (f'{ak[0]:b}' + f'{ak[1]:b}').count('1') < (f'{ak[2]:b}' + f'{ak[3]:b}').count('1'):
            fl = 1
            break
    if fl == 0:
        ans = a
        break

print(ans)
