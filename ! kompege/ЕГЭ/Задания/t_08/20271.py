n = '0123456789AB'
nech = '13579B'
from itertools import product

ans = 0
sp = []
for i in product(n, repeat=5):
    s = ''.join(i)
    if s[0] != '0':
        for j in nech:
            s = s.replace(j, '*')
        if s[0] not in nech and s[2] not in nech and s[4] not in nech and '*****' not in s and '****' not in s:
            ans += 1

print(ans)

#2 способ

import string
from itertools import product
a = (string.digits + string.ascii_uppercase)[:12]
nc = a[1::2]
ans = 0

for i in product(a, repeat=5):
    s = ''.join(i)
    for j in nc:
        s = s.replace(j, '*')
    if s[0] != '0' and s.count('**') <= 2 and '****' not in s:
        ans += 1

print(ans)
