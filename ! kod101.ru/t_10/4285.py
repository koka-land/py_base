from ipaddress import ip_network

network = ip_network('154.141.198.190/255.255.192.0', 0)

print(network[-1])
print(154 + 141 + 255 + 255)
print(sum(int(i) for i in str(network[-1]).split('.')))
