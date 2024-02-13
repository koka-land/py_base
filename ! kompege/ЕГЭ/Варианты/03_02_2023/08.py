from itertools import product

count = 0

for i in product('012345678', repeat=7):
    s = ''.join(i)
    if s[0] != '0':
        if s.count('8') == 1:
            if s[0] not in '1357':
                if s[-1] not in '02468':
                    count += 1

print(count)