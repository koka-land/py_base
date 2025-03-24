ans = 0

for n in range(1, 12):
    if n % 2 == 0:
        ans = max(ans, int('10' + bin(n)[2:], 2))
    else:
        ans = max(ans, int('1' + bin(n)[2:] + '01', 2))

print(ans)