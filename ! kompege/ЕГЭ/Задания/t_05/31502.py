sp = []

for n in range(1, 100):
    r = bin(n)[2:]
    if n % 2 == 0:
        r = '11' + r + '11'
    else:
        r = '1' + r + '00'
    r = int(r, 2)
    if r > 95:
        sp.append(r)
print(min(sp))

