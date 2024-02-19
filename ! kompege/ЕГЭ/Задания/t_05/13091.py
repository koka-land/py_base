sp = []

for n in range(1, 201):
    sp.append(int(bin(n)[2:] + bin(n % 4)[2:], 2))

otvet = 0
sp.sort()

for i in range(200 - 65):
    max_num = sp[i] + 65
    sp1 = []
    for j in range(65):
        if sp[i + j] < max_num:
            sp1.append(sp[i + j])
        else:
            break
    otvet = max(otvet, len(sp1))

print(otvet)



