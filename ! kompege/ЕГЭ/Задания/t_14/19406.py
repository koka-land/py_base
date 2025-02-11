import string
s = (string.digits + string.ascii_uppercase)[:35]

for x in s:
    a = int('6' + x + 'QR' + x, 35) + int(x + '59SH', 35) + int('PH' + x + '69YW', 35)
    max_c = 0
    max_k = 0
    a = str(a)
    for i in range(1, 10):
        if a.count(str(i)) >= max_k:
            max_k = a.count(str(i))
            max_c = i
    a = int(a)
    if a % (max_c**2) == 0:
        print(x, int(x, 35), a // (max_c**2))