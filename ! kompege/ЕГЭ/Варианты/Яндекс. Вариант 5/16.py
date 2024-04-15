import sys
sys.setrecursionlimit(5000)
from math import ceil
def f(x):
    if x <= 1:
        return 1
    if x % 2 == 0:
        return ceil(f(x - 1) * 1/3)
    else:
        return 6 * f(x - 1)

print(f(2049) / f(2046))