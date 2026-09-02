f = [int(i) for i in open('files/17_4416.txt')]
sp = []
for i in range(len(f) - 1):
    for j in range(i + 1, len(f)):
        a40 = 0
        if f[i] % 40 == 0:
            a40 +=1
        if f[j] % 40 == 0:
            a40 += 1
        if a40 != 0:
            if (f[i] + f[j]) % 60 == 0:
                sp.append(f[i] + f[j])
print(len(sp), max(sp))