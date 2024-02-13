min_r, min_n = 10**10, 10**10

for n in range(1, 200):
    r = bin(n)[2::]
    if (r.count('1') % 2) == 0:
        r = '1' + r[2::] + '0'
    else:
        r = '11' + r[2::] + '1'
    r = int(r, 2)
    if r > 49:
        if r < min_r:
            min_r = r
            min_n = n

print(min_n)
