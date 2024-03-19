sp = [0] * 2124

for i in range(len(sp) - 1, 0, -1):
    if i >= 2024:
        sp[i] = 1
    else:
        sp[i] = sp[i + 2] + sp[i + 4]

sp.pop(0)
print(len(set(sp)))

#2 способ (рекурсивный)

import sys
sys.setrecursionlimit(3000)
from functools import lru_cache
@lru_cache(maxsize=2000)
def f(n):
    if n >= 2024:
        return 1
    else:
        return f(n + 2) + f(n + 4)

sp = set()

for i in range(1, 2030):
    sp.add(f(i))

print(len(sp))

