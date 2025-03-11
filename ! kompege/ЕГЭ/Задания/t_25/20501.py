st2 = []
for i in range(1, 10**10):
    if 2 ** i < 10000:
        st2.append(2 ** i)
    else:
        break

ans = []

for c1 in range(10):
    for c2 in range(10):
        for c3 in st2:
            s = '8902' + str(c1) + str(c2) + str(c3)
            if int(s) % 1432 == 0:
                ans.append(int(s))

ans.sort()

for i in range(5):
    print(ans[i], ans[i] // 1432)