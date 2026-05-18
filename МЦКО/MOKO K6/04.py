p = 1024 * 280
v = 280 * 1024 * 8
from math import *
for n in range(1, 10**10):
    i = ceil(log2(n))
    i = i + 3
    if p * i <= v:
        print(n)
    else:
        break