ans = 0

for n in range(1, 313, 2):
    r = bin(n)[2:]
    if n % 5 == 0:
        r = r[:3] + r
    else:
        r = r + bin((n % 5) * 5)[2:]
    r = int(r, 2)
    if r < 313:
        if n > ans:
            ans = n

print(ans)
