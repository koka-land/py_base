a = 4**151 + 7**283 + 6**82
for x in range(1, 3053):
    b = a - 5 * x
    b8 = ''
    while b > 0:
        b8 = str(b % 8) + b8
        b //= 8
    if b8.count('1') == 26:
        print(x)
        break