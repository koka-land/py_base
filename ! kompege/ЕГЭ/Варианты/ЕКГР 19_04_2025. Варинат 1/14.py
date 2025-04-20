ansx = 0
ans0 = 5**210

for x in range(2000, 0, -1):
    a = 4 ** 210 + 4 ** 110 - x
    s = ''
    while a > 0:
        s = str(a % 4) + s
        a = a // 4
    if s.count('0') < ans0:
        ans0 = s.count('0')
        ansx = x

print(ansx)

a = 2000
s = ''
while a > 0:
    s = str(a % 4) + s
    a = a // 4
print(s)

print(int('122223', 4))