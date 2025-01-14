from fnmatch import *
for n in range(18579, 10 ** 10 + 1, 18579):
    if fnmatch(str(n), '54?1?3*7'):
        print(n, n // 18579)