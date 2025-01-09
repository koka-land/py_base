from itertools import product
s = '0123456789abcdefghijklmno'
ans = 0

for i in product(s, repeat=4):
    n = ''.join(i)
    nc = 0
    m5 = 0
    if n[0] != '0':
        for j in n:
            if int(j, 25) % 2 != 0:
                nc += 1
            if int(j, 25) <= 5:
                m5 += 1
        if nc == 1 and m5 <= 2:
            ans += 1

print(ans)

