s = '0123456789AB'

for x in s:
    a = int(f'154{x}3', 12)
    b = int(f'1{x}365', 12)
    c = a + b
    if c % 13 == 0:
        print(x, c // 13)