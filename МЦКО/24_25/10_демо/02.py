ans = []

for n in range(200):
    r = bin(n)[2:]
    if n % 2 == 0:
        r += '10'
    else:
        r = '1' + r + '00'
    r = int(r, 2)
    if r > 107:
        ans.append(n)

print(min(ans))