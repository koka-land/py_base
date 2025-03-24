from itertools import product
s = '0123456789AB'
c = 0

for i in product(s, repeat=5):
    a = ''.join(i)
    if a[0] != '0' and a.count('7') == 1 and (a.count('9') + a.count('A') + a.count('B') <= 3):
        c += 1

print(c)