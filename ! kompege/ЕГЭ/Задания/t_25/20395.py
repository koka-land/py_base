from itertools import product
s = '0123456789'

for i in range(2):
    for l in s:
        for j in product(s, repeat = i):
            a = int('1' + l + '7301' + ''.join(j) + '320')
            if (a % 8 == 0) and (a % 30 == 0) and (a % 42 == 0):
                print(a, a // 8)