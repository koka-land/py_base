count = 0
ans = 0
sp = []
max43 = -10**10

for i in open('files/17_27629.txt'):
    sp.append(int(i))
    if i[-2:] == '43' and len(str(abs(int(i)))) == 4:
        max43 = max(max43, int(i))

for i in range(len(sp) - 1):
    if len([sp[i + j] for j in range(2) if len(str(abs(sp[i + j]))) == 4]) != 0:
        if (sp[i] + sp[i + 1])**2 < max43**2:
            count += 1
            ans = max(ans, (sp[i] + sp[i + 1])**2)

print(count)
print(ans)