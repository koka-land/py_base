from math import *
for c in range(2, 10**10):
    if ceil((ceil(log2(c)) * 157) / 8) * 12450 <= 955 * 1024:
        print(c)
    else:
        break