import re
def f(a):
    for u in range(2, int(a**0.5 + 1)):
        if a % u == 0:
            return 0
    return 1

sp = []
for i in range(2, 10**5 + 1):
    if f(i):
        sp.append(i)
print(sp)

for i in sp:
    if (sp.index(i) + 1) in sp:
        if re.fullmatch(r'1\d*7\d7', str(i)):
            print(i, sp.index(i) + 1)