def st2(x):
    i = 0
    while 2 ** i < x:
        i += 1
    return i

from math import ceil

for n in range(1, 10**10):
    i = st2(n)
    if (ceil(2783 * i / 8) * 62784) / 1024**2 >= 356:
        print(n)
        break