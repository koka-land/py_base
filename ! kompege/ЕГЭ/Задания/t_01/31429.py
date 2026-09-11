from itertools import permutations

n = '1256 123 2345 3456 1345 146'.split()
c = 'FC CB BE EA AF DF DB DE'.split()
print(n)
print(c)
for a, b in c:
    print(a, b)
print(*range(1, 7))
for p in permutations('ABCDEF'):
    if all(str(p.index(b) + 1) in n[p.index(a)] for a, b in c):
        print(*p)