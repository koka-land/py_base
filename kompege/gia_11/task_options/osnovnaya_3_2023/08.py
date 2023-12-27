from itertools import product

ch = '02468ACE'
count = 0

for a1, a2, a3 in product('0123456789ABCDEF', repeat=3):
    s = a1 + a2 + a3
    if s[0] != '0':
        if (s[0] in ch and s[1] not in ch and s[2] in ch) or (s[0] not in ch and s[1] in ch and s[2] not in ch):
            if s[0] != s[2]:
                count += 1

print(count)