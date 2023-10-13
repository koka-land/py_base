from itertools import product
import time

s123 = time.time()
max2 = 0

for pol in range(1, 30):
    sp = []
    for sp in product('12', repeat=pol):
        sp1 = []
        if sp.count('1') == sp.count('2'):
            sp1.append(''.join(sp))
        for i in sp1:
            s = '0' + i + '0'
            while '00' not in s:
                s = s.replace('011', '20', 1)
                s = s.replace('022', '10', 1)
                s = s.replace('02', '110', 1)
                s = s.replace('01', '220', 1)
            if s.count('1') == 47 and s.count('2') < 70:
                max2 = max(max2, s.count('2'))

e123 = time.time()
print(max2, e123 - s123)