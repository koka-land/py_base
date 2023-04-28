ans = []

for i in range(10**6):
    r = bin(i)[2::]
    if i % 5 == 0:
        r += bin(5)[2::]
    else:
        r += '1'
    n = int(r, 2)
    r = bin(n)[2::]
    if n % 7 == 0:
        r += bin(7)[2::]
    else:
        r += '1'
    n = int(r, 2)
    if n < 1728404:
        ans.append(i)

print(max(ans))