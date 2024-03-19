import sys
sys.setrecursionlimit(3000)
from functools import lru_cache
@lru_cache(maxsize=2000)
def f(n):
    if n <= 1: #Если оставить 0.5, значение функций после 169 = inf
        return 1
    else:
        return (n + 1) * f(n - 1)

print(f(200) / f(198))