sp = []
for n in range(200):
    r = bin(n)[2:]
    if n % 2 != 0:
        r = '1' + r + '0'
    else:
        r = '11' + r + '11'
    r = int(r, 2)
    if r < 126:
        sp.append(r)

print(max(sp))