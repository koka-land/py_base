x = 101330
s = ''
while x > 0:
    s = str(x % 3) + s
    x //= 3
print(s)
print(int('12011000001', 3))