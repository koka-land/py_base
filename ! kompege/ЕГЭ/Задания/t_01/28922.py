from itertools import *

n = '147 2458 367 1245 2456 356 1378 278'.split()
c = 'AB AH BC BG CD DF HF EF GC GE'.split()
print(*range(1, 9))
for p in permutations('ABCDEFGH'):
    if all(str(p.index(b) + 1) in n[p.index(a)] for a, b in c):
        print(*p)