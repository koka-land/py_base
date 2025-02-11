import string
s = (string.digits + string.ascii_uppercase)[:25]

for x in s:
    a = int('11353' + x + '12', 25) + int('135' + x + '21', 25)
    if a % 24 == 0:
        print(x, int(x, 25), a // 24)
