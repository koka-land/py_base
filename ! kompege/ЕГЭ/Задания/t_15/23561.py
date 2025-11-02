ans = []
for a in range(1, 1800):
    for x in range(1, 1801):
        if ((x % 128 == 0) <= ((x % a != 0) <= (x % 80 != 0))) == 0:
            break
    if x == 1800:
        ans.append(a)
print(max(ans))