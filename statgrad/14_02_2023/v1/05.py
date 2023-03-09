st = int(bin(123456789)[2:-3:], 2)
en = int(bin(1987654321)[2:-3:], 2)
print(st, en)
st1 = 123456789
en1 = 1987654321
sp = []

for n in range(st, st + 100):
    for r in range(3):
        a = [int(i) for i in str(n)]
        summ = sum(a)
        n = bin(n)[2::]
        if summ % 2 == 0:
            n = n + '0'
        else:
            n = n + '1'
        n = int(n, 2)
    if n in range(st1, en1):
        sp.append(n)
list(set(sp))
print(len(sp), sp)
