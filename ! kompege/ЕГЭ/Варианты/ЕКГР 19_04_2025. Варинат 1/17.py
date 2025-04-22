f = open('files/17.txt')
max5 = 0
sp = []
ans1 = 0
ans2 = 0

for i in f:
    sp.append(int(i))
    if int(i) > 0 and len(i) == 4 and int(i) % 10 == 5:
        max5 = max(max5, int(i))

for i in range(len(sp) - 1):
    a5 = 0
    summ = 0
    for j in range(2):
        if sp[i + j] % 10 == 5 and len(str(abs(sp[i + j]))) == 4:
            a5 += 1
        summ += sp[i + j]
    if a5 > 0 and summ > max5:
        ans1 += 1
        ans2 = max(ans2, summ)

print(ans1, ans2)
