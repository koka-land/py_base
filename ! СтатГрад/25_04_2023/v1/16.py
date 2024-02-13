def F(n):
    if n > 1000000:
        return n
    else:
        return n + F(2 * n)

def G(n):
    return F(n) / n

x = G(1000)

count = 0

for i in range(1, 10000):
    if G(i) == x:
        count += 1

print(count)