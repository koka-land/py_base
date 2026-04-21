f = open('files/17_27301.txt')
sp = []
max45 = -10**10

for i in f:
    sp.append(int(i))
    if str(abs(int(i)))[:2] == '45':
        max45 = max(int(i), max45)

ans1 = 0
ans2 = 10**10

for i in range(len(sp) - 2):
    otr = 0
    sum_ = 0
    for j in range(3):
        if sp[i + j] < 0:
            otr += 1
        sum_ += sp[i + j]
    if otr == 1 and sum_ >= max45:
        ans1 += 1
        if str(sum_)[-2:] == '45':
            ans2 = min(ans2, sum_)

print(ans1)
print(ans2)