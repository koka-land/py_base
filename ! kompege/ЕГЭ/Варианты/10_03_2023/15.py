ans = []

for a in range(1, 100):
    f = 0
    for x in range(1, 120):
        for y in range(1, 120):
            if (((x + y) <= 32) or (y <= (x + 4)) or (y >= a)) == False:
                f = 1
                break
        if f == 1:
            break
    if f == 0:
        ans.append(a)

print(max(ans))