from itertools import permutations

s = '4' * 8 + '2' * 5
m = set()

for i in permutations(s, 6):
    m.add(''.join(i))

print(m)

