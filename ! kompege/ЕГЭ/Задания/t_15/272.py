ans = 0

for A in range(1, 200):
    f = 0
    for x in range(1, 200):
        for y in range(1, 200):
            if (((x > 8) <= ((x**2 + 3 * x) >= A)) and (((y**2 + 5 * y) > A) <= (y >= 4))) == 0:
                f = 1
                break
        if f == 1:
            break
    if f == 0:
        ans += 1

print(ans)