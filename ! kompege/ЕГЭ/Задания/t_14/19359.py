import string
s = string.digits + string.ascii_lowercase[:12]
for x in s:
    a = int('a23' + x + 'ac0', 22)
    b = int('gb' + x + '21670', 22)
    c = a + b
    if c % 21 == 0:
        print(x, int(x, 22), c / 22)