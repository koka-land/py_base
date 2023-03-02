a = 3*1024**75 + 2*256**76 - 16**77 - 2023
k = 0
sym = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s = ''
while a > 0:
    s = sym[a % 32] + s
    if a % 32 == 0:
        k += 1
    a = a // 32
print(k)
print(s)
print(s.count('0'))