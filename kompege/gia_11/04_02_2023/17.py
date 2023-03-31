f = open('files/17.txt', 'r')
sp = []
max_9 = -(10 ** 10)
count = 0

for i in f:
    sp.append(int(i))
    if (int(i) > max_9) and (abs(int(i)) % 10 == 9):
        max_9 = int(i)

max_9 = max_9 ** 2
min = max_9

for i in range(len(sp) - 1):
    if ((abs(sp[i]) % 10 == 9) and (abs(sp[i+1]) % 10 != 9)) or ((abs(sp[i]) % 10 != 9) and (abs(sp[i+1]) % 10 == 9)):
        if (sp[i]**2 + sp[i+1]**2) < max_9:
            count += 1
            if (sp[i]**2 + sp[i+1]**2) < min:
                min = (sp[i]**2 + sp[i+1]**2)

print(count, min)