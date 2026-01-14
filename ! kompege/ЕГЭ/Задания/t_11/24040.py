c = 10 + 52 + 1989

for j in range(2, 50):
    if 2**j >= c:
        i = j
        break

ans = []

for d in range(1, 1000):
    if (((d * i) / 8) * 836) / 1024 > 639:
        print(max(ans))
        break
    else:
        ans.append(d)