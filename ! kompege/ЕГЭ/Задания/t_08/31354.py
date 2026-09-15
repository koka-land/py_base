from itertools import product
s = 'ЕЛНОСЦ'
s1 = 'ЦН'
n = 0
sp = []

for i in product(s, repeat=6):
    n += 1
    w = ''.join(i)
    if n % 2 == 1 and w[0] not in s1 and w.count('Ц') == 1 and w.count('Н') == 1:
        sp.append(n)
print(sp[-1])