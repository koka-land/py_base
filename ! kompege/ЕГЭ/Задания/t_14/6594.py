s = '0123456789ABC'

for x in s:
    a = int(f'753{x}2', 13)
    b = int(f'2{x}173', 13)
    c = a + b
    if c % 12 == 0:
        print(x, c // 12)