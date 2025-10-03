a = 9 * 11**210 + 8 * 11**150
ans = []

for x in range(1, 3001):
    b = a - x
    c = 0
    while b > 0:
        if b % 11 == 0:
            c += 1
        b //= 11
    if c == 60:
        ans.append(x)

print(max(ans))