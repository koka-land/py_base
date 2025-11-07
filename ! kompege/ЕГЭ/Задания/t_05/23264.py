def v3(x):
    ans = ''
    while x > 0:
        ans = str(x % 3) + ans
        x //= 3
    return ans

ans = []

for n in range(1, 200):
    r = v3(n)
    if n % 3 == 0:
        r += r[-2:]
    else:
        r += v3((n % 3) * 5)
    r = int(r, 3)
    if r > 150:
        ans.append(r)

print(min(ans))