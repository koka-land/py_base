from math import ceil

d = 64
s = 26 * 2
b = 1

while 2 ** b < s:
    b += 1
bit = d * b
byte = ceil(bit / 8) + 64
kbyte = (byte * 768) // 1024

print(kbyte)
