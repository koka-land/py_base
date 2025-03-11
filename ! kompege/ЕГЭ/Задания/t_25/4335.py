from fnmatch import *

ans = 0
def div(x):
    d = set()
    for i in range (1, int(x**0.5) + 1):
        if x % i == 0:
            d.add(i)
            d.add(x // i)
    d = sorted(list(d))
    return d

def prime(x):
    f = 0
    for i in range (2, int(x**0.5) + 1):
        if x % i == 0:
            f = 1
            break
    return f

for i in range (960001, 10**10):
    sp = div(i)
    d3 = 0
    s3 = 0
    for j in sp:
        if fnmatch(str(j), '*3?'):
            if prime(j) == 0:
                d3 += 1
                s3 += j
    if d3 > 2:
        print(i, s3)
        ans += 1
    if ans == 5:
        break