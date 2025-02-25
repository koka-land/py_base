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