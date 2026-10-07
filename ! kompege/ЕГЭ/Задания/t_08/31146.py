from itertools import product
s = 'АЕЛНПР'
n = 0
ans = 0

for i in product(s, repeat=6):
    n += 1
    w = ''.join(i)
    if w.count('П') == 0 and w.count('Р') == 0 and w.count('А') == 2 and w.count('Н') == 1:
        ans = n

print(ans)
