import string
a = (string.digits + string.ascii_uppercase)[:23]
for x in a:
    b = int(f'761{x}035', 23) + int(f'338{x}932', 23)
    if b % 22 == 0:
        print(x, b // 22)
        break
