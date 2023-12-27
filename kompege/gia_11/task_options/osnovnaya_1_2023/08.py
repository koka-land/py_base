from itertools import product
nomer = 0
iskomiy_nomer = 0

for a1, a2, a3, a4, a5, a6 in product('АГМНСТУ', repeat=6):
    nomer += 1
    s = a1 + a2 + a3 + a4 + a5 + a6
    if s[0] != 'У':
        if s.count('М') == 2:
            if s.count('Г') <= 1:
                iskomiy_nomer = nomer

print(iskomiy_nomer)