sp = []

for n in range (1, 225):
    r = bin(n)[2::]
    if n % 2 == 0:
        r = '1' + r + '0'
    else:
        r = '11' + r + '11'
    r = int(r, 2)
    if r > 225:
        print(r)
        sp.append(r)

print(min(sp))