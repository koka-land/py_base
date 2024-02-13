for x in range(2, 100):
    p1 = '3' + str(x) + '51'
    p2 = '1' + str(x) + '3'
    a = 3 * 15**4 + x * 15**3 + 1 * 15**2 + 5 * 15 + x
    b = 1 * int(p1)**2 + 2 * int(p1) + 3
    c = x**x
    d = 1 * int(p2)**2 + x * int(p2) + 3
    e = 1 * (x+1)**2 + x * (x+1) + 2
    otv = a + b + c + d + e
    if (otv) % 13 == 0:
        print(otv)
        break

s = '0123456789ABC'
super_otv = ''

while otv > 0:
    super_otv = s[otv % 13] + super_otv
    otv //= 13

print(super_otv)
