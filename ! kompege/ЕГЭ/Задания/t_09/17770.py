f = open('files/9_17770.csv')
ans = 0

for i in f:
    sp = [int(x) for x in i.split(';')]
    sp.sort()
    sp5 = [x for x in sp if x % 10 == 5]
    if sum(sp[-2:]) * 2 > sum(sp[:3]) * 3 and len(sp5) >= 2:
        ans += 1

print(ans)