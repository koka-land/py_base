from ipaddress import *

net = ip_network('218.194.82.148/255.255.255.192', 0).hosts()
print(max(net))