a = 1024**24 + 444**14 + 388**8

sp = []

while a > 0:
    sp.append(a % 9)
    a //= 9

print(sp.count(max(sp)))