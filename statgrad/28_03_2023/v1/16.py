def f(a, b):
    if b == 0:
        return a
    if a >= b > 0:
        return f(a - b, b)
    if a < b:
        return f(b, a)

count = 0
start = 123456795
stop = 1234567888

for n in range (0, 14):
    if f(n, 14) == 1:
        count += 1

print((stop - start) // 14 * count)

