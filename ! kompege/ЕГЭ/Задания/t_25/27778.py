print('fnmatch')
from fnmatch import *
for n in range(271, 10 ** 8 + 1, 271):
    if fnmatch(str(n), '12??15*6'):
        print(n, n // 271)

print('re.fullmatch')
from re import fullmatch
for n in range(271, 10 ** 8 + 1, 271):
    if fullmatch(r'12[0-9][0-9]15[0-9]*6', str(n)):
        print(n, n // 271)