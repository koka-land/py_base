from itertools import *

n = '258 17 56 68 138 347 26 145'.split()
c = 'HD DA AC CB BH HF FE EG GA GC'.split()
print(*range(1, 9))
for p in permutations('ABCDEFGH'):
    if all(str(p.index(b) + 1) in n[p.index(a)] for a, b in c):
        print(*p)