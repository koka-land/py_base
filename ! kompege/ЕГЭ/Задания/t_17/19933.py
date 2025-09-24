f = open('files/17_19933.txt')

sp = []
mp12 = 10**10
count = 0
all_p = []
all_s = []

for i in f:
    sp.append(int(i))
    if 0 < int(i) < mp12 and int(i) %12 == 0:
        mp12 = int(i)

for i in range(len(sp) - 2):
    p = 0
    s = 1
    for j in range(3):
        if sp[i + j] % 506 == 0:
            if len(str(abs(sp[i + j]))) == 5:
                p += 1
        s *= sp[i + j]

    if p > 0 and abs(s) % 100 == mp12:
        all_p.append([sp[i + 0], sp[i + 1], sp[i + 2]])
        all_s.append(abs(sum(all_p[-1])))

print(len(all_p))
print(min(all_s))
