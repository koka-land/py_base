s = 'АКЛМНЯ'
num = 1

from itertools import product

for a1, a2, a3, a4, a5 in product(s, repeat=5):
    str = a1 + a2 + a3 + a4 + a5
    if str[0:2] == 'КМ':
        print(num, str)
        break
    num += 1

