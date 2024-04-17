f = open('files/17_14952.txt')
sp = []
max121 = 0
for i in f:
    sp.append(int(i))
    if int(i) % 1000 == 121:
        max121 = max(int(i), max121)

otvet1, otvet2 = 0, 0

for i in range(len(sp) - 2):
    ch = 0
    sum = 0
    for j in range(3):
        if sp[i + j] % 2 == 0 and len(str(abs(sp[i + j]))) == 4:
            ch += 1
        sum += sp[i + j]
    if ch <= 1 and sum < max121:
        otvet1 += 1
        otvet2 = max(otvet2, sum)

print(otvet1, otvet2)