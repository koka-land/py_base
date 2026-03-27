from fnmatch import *
for n in range(271, 10 ** 8 + 1, 271):
    if fnmatch(str(n), '12??15*6'):
        print(n, n // 271)