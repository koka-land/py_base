for i in range(2, 50):
    if (((i * 105) / 8) * 65536) / 1024**2 >= 7:
        print(2**(i - 1) + 1)
        break


def podbor(x):
    i = 1
    while 2**i < x:
        i += 1
    return(i)

import math

for a in range(1, 10**10):
    if (((math.ceil(math.log(a, 2)) * 105) / 8) * 65536) / 1024 ** 2 >= 7:
    #if (((podbor(a) * 105) / 8) * 65536) / 1024 ** 2 >= 7:
        print(a)
        break