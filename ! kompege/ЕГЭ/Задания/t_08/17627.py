from itertools import product
s = '0123456789ABCDE'
a = 0
for i in product(s, repeat=5):
    c = ''.join(i)
    if c.count('8') == 1 and c[0] != '0' and (c.count('A') + c.count('B') + c.count('C') + c.count('D') + c.count('E') >= 2):
        a += 1

print(a)
