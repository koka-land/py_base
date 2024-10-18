from itertools import product

a = 'ЮА'
ans = 0

for i in product('ЛЮСТРА', repeat=5):
    s = ''.join(i)
    if s.count('Ю') <= 2 and s[4] in a:
        ans += 1

print(ans)
