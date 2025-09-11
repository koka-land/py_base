'''1 способ'''
import string
s = (string.digits + string.ascii_uppercase)[:29]

for x in s:
    a = int('923' + x + '874', 29) + int('524' + x + '6152', 29)
    if a % 28 == 0:
        print(x, a // 28)

'''2 способ'''
a = int('9230874', 29) + int('52406152', 29)
for i in range(29):
    if a % 28 == 0:
        print(i, a // 28)
    a += 29**3 + 29**4