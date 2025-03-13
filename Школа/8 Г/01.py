c = 0

for a in range(1000, 10000):
    s = sorted([int(str(a)[0]) * int(str(a)[1]), \
                int(str(a)[1]) * int(str(a)[2]), \
                int(str(a)[2]) * int(str(a)[3])])
    if len(str(int(str(s[0]) + str(s[1]) + str(s[2])))) == 4:
        c += 1

print(c)