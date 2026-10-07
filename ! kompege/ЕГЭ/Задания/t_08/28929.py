from itertools import product
s = 'ВИЛМОС'
s1 = 'ОС'
ans = 0
n = 0

for i in product(s, repeat=5):
    n += 1
    w = ''.join(i)
    if n % 2 != 0 and w[0] not in s1 and w.count('В') == 1 and w.count('С') <= 1:
        ans = n

print(ans)