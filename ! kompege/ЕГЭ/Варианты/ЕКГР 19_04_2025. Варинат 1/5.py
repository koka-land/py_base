sp = []

for n in range(11, 100):
    r = bin(n)[2::]
    if n % 2 == 0:
        r = '10' + r
    else:
        r = '1' + r + '01'
    sp.append(int(r, 2))

print(min(sp))
