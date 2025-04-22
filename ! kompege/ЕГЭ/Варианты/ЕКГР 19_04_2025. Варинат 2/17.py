f = open('files/17.txt')
min6 = 10**10
sp = []
ans1 = 0
ans2 = -300000

for i in f:
    sp.append(int(i))
    if sp[-1] > 0 and len(str(sp[-1])) == 4 and sp[-1] % 10 == 6:
        min6 = min(min6, int(i))

for i in range(len(sp) - 2):
    a6 = 0
    a4 = 0
    summ = 0
    for j in range(3):
        if abs(sp[i + j]) % 10 == 6 and len(str(abs(sp[i + j]))) == 4:
            a6 += 1
        summ += sp[i + j]
    if a6 == 1 and summ <= min6:
        ans1 += 1
        ans2 = max(ans2, summ)

print(ans1, ans2)
