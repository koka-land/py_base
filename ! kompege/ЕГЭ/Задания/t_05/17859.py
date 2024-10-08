max_r = 0

for n in range(12):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '01'
    r = int(r, 2)
    if r > max_r:
        max_r = r

print(max_r)

