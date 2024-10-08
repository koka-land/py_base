from itertools import product
from time import *

st = time()
maxsumm = 0
ans = ''

for i in product('24', repeat=65):
    s = ''.join(i)
    s = '3' + s + '3'
    s1 = s
    if s.count('4') == 40 and s.count('2') == 25:
        while '3' in s:
            if '342' in s:
                s = s.replace('342', '4123', 1)
            if '34' in s:
                s = s.replace('34', '413', 1)
            if '32' in s:
                s = s.replace('32', '13', 1)
            if '33' in s:
                s = s.replace('33', '424', 1)

        summ = 0
        for i in s:
            summ += int(i)
        if summ > maxsumm:
            maxsumm = summ
            ans = s1

print(maxsumm)
print(ans)
et = time()
print(et - st)
