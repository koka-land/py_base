s = ''

for i in range(10):
    s += str(i)
for i in range(ord('A'), ord('Z') + 1):
    s += chr(i)

a = int(input('Введите число в десятичной системе счисления: '))
ss = int(input('Введите систему счисления, в которую переводим: '))

otvet = ''

while a > 0:
    if a % ss < len(s):
        otvet = s[a % ss] + otvet
    else:
        otvet = '*' + otvet
    a //= ss

print(otvet)