max_n = 0
min_r = 10**10

for n in range(1, 140):
    r = bin(n)[2:]
    if n % 3 == 0:
        r += r[-3:]
    else:
        r += bin((n % 3) * 3)[2:]
    r = int(r, 2)
    if abs(130 - r) <= min_r:
        min_r = 130 - r
        max_n = n

print(max_n)

