from itertools import product
s = 'АЕЛПРЬ'
n = 0
for i in product(s, repeat=6):
    n += 1
    w = ''.join(i)
    if w[0] != 'А' and w[0] != 'Л' and w.count('П') >= 2:
        if n % 2 != 0:
            print(n, w)
            break

