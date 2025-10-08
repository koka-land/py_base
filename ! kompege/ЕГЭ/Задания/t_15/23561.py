ans = []
for a in range(1, 2000):
    for x in range(1, 2001):
        if ((x % 128 == 0) <= ((x % a != 0) <= (x % 80 != 0))) == 0:
            break
    if x == 2000:
        ans.append(a)
print(ans)