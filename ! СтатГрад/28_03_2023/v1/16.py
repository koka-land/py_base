def f(a, b):
    if b == 0:
        return a
    if a >= b > 0:
        return f(a - b, b)
    if a < b:
        return f(b, a)

for i in range(1, 100):
    if f(i, 14) == 1:
        print(i)

count = 0
start = 123456795
stop = 1234567888

for n in range(0, 14):
    #print(n, f(n, 14))
    if f(n, 14) == 1:
        count += 1

print((stop - start) // 14 * count)

# Решение без функции

count = 0
for i in range(start, stop + 1, 2):
    if i % 7 != 0:
        count += 1
print(count)