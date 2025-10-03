a = 15625**16 - 3125**3 * 25**19 + 625**4 - 2005

ans = 0

while a > 0:
    if a % 5 == 0:
        ans += 1
    a //= 5

print(ans)