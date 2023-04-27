sp = []
max_n = 0

for n in range(4, 100):
    r = bin(n)[2::]
    if n % 3 == 0:
        r += r[-3::]
    else:
        r += bin(3 * (n % 3))[2::]
    if int(r, 2) < 100:
        sp.append(n) #1 способ. Список
        max_n = max(max_n, n) #2 способ. Максимум

print(max(sp))
print(max_n)