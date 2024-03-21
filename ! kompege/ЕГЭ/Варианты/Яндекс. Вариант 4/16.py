sp = [0, 2]

for i in range(2, 5000000):
    if sp[i - 1] < 7555444:
        sp.append(sp[i - 1] + 6)
    else:
        sp.append(sp[i - 1] - 7555444)

print(max(sp))

#2 способ

sp = [2]
maxx = 0
f = 0
while f == 0:
    a = sp[-1]
    while a < 7555444:
        a += 6
    maxx = max(maxx, a)
    if (a - 7555444) in sp:
        f = 1
    else:
        sp.append(a - 7555444)

print(maxx)