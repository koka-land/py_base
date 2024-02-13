from itertools import product

count = 0

for a1, a2, a3, a4, a5 in product('012345678', repeat=5):
    s = a1 + a2 + a3 + a4 + a5
    if s[0] != '0':
        if s.count('5') == 1:
            if s[0] != s[1] and s[1] != s[2] and s[2] != s[3] and s[3] != s[4]:
                count += 1

print(count)