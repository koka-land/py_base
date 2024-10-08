from itertools import product
c = 0
for i in product('01', repeat=11):
    s = ''.join(i)
    if s.count('1') == 7:
        c += 1
print(c)