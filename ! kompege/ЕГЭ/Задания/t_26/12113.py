f = open('files/26_12113.txt')
n = int(f.readline())
sp = []

for i in f:
    sp.append([int(i), int(i) % 2])

sp = sorted(sp, reverse=True)
otvet = 0

for i in range(50):
    box_n = sp[i]
    count = 1
    for j in range(i, n):
        if box_n[0] - sp[j][0] >= 7:
            if box_n[1] != sp[j][1]:
                count += 1
                box_n = sp[j]
                min_b = sp[j][0]
    if count > otvet:
        otvet = count
        min_b = box_n[0]

print(otvet, min_b)

