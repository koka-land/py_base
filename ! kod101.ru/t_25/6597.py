a = 7 * 13 * 17 * 23 * 29
for i in range(10**9, 2*10**9 +1):
    if i % a == 0:
        start = i
        break
def div(x):
    d = set()
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            if i % 2 != 0: d.add(i)
            if (x // i) % 2 != 0: d.add(x // i)
    return d

ans = 0

for i in range(start, 2 * 10**9 + 1, a):
    if i % 3 != 0:
        if i % 5 != 0:
            if len(div(i)) > 100:
                ans += 1

print(ans)
