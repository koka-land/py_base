a = int(input())
sp = [1, a]

for i in range(2, int(a ** (1 / 2)) + 1):
    if a % i == 0:
        sp.extend((i, a // i))

sp = sorted(list(set(sp)))

print(sp)
