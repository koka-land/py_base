from itertools import permutations
s = 'МАКАКА'
ans = set()

for i in permutations(s):
    s = ''.join(i)
    if 'АА' not in s and 'КК' not in s:
        ans.add(s)

print(len(ans))