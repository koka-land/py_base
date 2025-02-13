from itertools import product

a = '0123456789AB'
b = '9AB'
c = 0

for i in product(a, repeat=5):
    s = ''.join(i)
    if s[0] != '0' and s.count('7') == 1 and len([i for i in s if i in b]) <= 3:
        c += 1
        print(s)

print(c)
