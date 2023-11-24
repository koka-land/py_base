from fnmatch import *
for n in range(8387, 10 ** 9 + 1, 8387):
    if fnmatch(str(n), '*75?122*'):
        print(n, n // 8387)
