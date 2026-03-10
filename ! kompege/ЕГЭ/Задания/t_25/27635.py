from fnmatch import *
for n in range(171, 10 ** 8 + 1, 171):
    if fnmatch(str(n), '1*23??56'):
        print(n, n // 171)