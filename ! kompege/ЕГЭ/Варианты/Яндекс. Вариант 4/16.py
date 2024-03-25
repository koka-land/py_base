sp = [0, 2]

for i in range(2, 5000000):
    if sp[i - 1] < 7555444:
        sp.append(sp[i - 1] + 6)
    else:
        sp.append(sp[i - 1] - 7555444)

print(max(sp))

#2 способ

sp = [2]
maxx = 0
f = 0
while f == 0:
    a = sp[-1]
    while a < 7555444:
        a += 6
    maxx = max(maxx, a)
    if (a - 7555444) in sp:
        f = 1
    else:
        sp.append(a - 7555444)

print(maxx)

#3 способ
from functools import lru_cache
@lru_cache(10000)

def f(n):
    if n == 1:
        return 2
    if ((n > 1) and (f(n-1) < 7555444)):
        return f(n-1) + 6
    else:
        return f(n-1) - 7555444

sp = []

for i in range(1, 3000000):
    sp.append(f(i))

print(max(sp))