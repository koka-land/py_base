import string
d = (string.digits + string.ascii_uppercase)[:22]

for x in d:
    a = int(f'27{x}98966', 22) + int(f'26{x}33', 22) + int(f'522{x}5', 22)
    if a % 21 == 0:
        print(x, a // 21)