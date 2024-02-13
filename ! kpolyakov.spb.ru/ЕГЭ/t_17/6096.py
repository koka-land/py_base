f = open('files/17-362.txt', 'r')
sp = []
alph = []
count = 0
max_summ = 0

for i in f:
    sp.append(i[:-1:])

for i in range(10):
    alph.append(str(i))
for i in range(ord('A'), ord('Z') + 1):
    alph.append(chr(i))

def ss(x):
    max_c = 0
    for i in x:
        max_c = max((alph.index(i) + 1), max_c)
    return max_c

for i in range(len(sp) - 1):
    a = ss(sp[i])
    b = ss(sp[i + 1])
    if abs(a - b) <= 2:
        count += 1
        max_summ = max((int(sp[i], a) + int(sp[i + 1], b)), max_summ)

print(count, max_summ)