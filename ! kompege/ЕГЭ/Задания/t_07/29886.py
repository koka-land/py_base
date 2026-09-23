from math import *
wh = 1024 * 768
max_n = 0
for n in range(1, 10**10):
    i = ceil(log2(n))
    v = ((wh * i) / 8 / 1024) + 4
    if v == 1540:
        if n > max_n:
            max_n = n
    if v > 1540:
        print(max_n)
        break











