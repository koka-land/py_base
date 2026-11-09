import string
c = (string.digits + string.ascii_uppercase)[:22]

for x in c:
    a = int(f'27{x}98876', 22) + int(f'26{x}51', 22) + int(f'711{x}5', 22)
    if a % 21 == 0:
        print(a // 21)
        break


