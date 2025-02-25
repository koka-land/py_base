lst = []

for n in range(4, 1000):
    r = bin(n)[2::]
    if n % 2 == 0:
        r = r + r[0:3]
    else:
        r = '1' + r + '01'
    r = int(r, 2)
    if r > 600:
        lst.append(r)

print(min(lst))