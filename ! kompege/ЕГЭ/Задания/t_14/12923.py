a = 3 * 3125**9 + 2 * 625**8 - 4 * 625**7 + 3 * 125**6 - 2 * 25**5 - 2024
b = a

#1 способ

c0 = 0

while a > 0:
    if a % 25 == 0:
        c0 += 1
    a //= 25

print(c0)

#2 способ

ci = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
otvet = ''

while b > 0:
    otvet = ci[b % 25] + otvet
    b //= 25

print(otvet.count('0'))