from itertools import product
s = 'АВНРЬЯ'
pn = 1
ans = 0

for i in product(s, repeat=5):
    w = ''.join(i)
    if w[0] != 'Я':
        if w.count('Ь') <= 1:
            if 'ЯЯ' not in w:
                ans = pn
    pn += 1

print(ans)

