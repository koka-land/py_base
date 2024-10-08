r_min = 10**10

for i in range(1, 1000):
    n = format(i, 'b')
    if n.count('1') % 2 == 0:
        n += '11'
    else:
        n += '01'
    r = int(n, 2)
    if r > 61:
        r_min = min(r, r_min)

print(r_min)