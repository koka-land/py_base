f = open('files/17_25356.txt')

sp = []
max30 = -100000
ans1 = 0
ans2 = -10**10

for i in f:
    sp.append(int(i))
    if (sp[-1] % 100 == 30) and (sp[-1] > max30):
        max30 = sp[-1]

for i in range(len(sp) - 2):
    c4 = 0
    sum3 = 0
    for j in range(3):
        if len(str(abs(sp[i + j]))) == 4:
            c4 += 1
        sum3 += sp[i + j]
    if c4 == 0 and sum3 > max30:
        ans1 += 1
        ans2 = max(ans2, sum3)

print(ans1)
print(ans2)
