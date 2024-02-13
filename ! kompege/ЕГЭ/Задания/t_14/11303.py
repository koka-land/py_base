s = '0123456789ABCDEFGHIJ'

for x in s:
    a = int('627' + x + 'J8', 20)
    b = int('H45I' + x + '5HIJ', 20)
    c = int('4IDB49J' + x + '7', 20)
    n = a + b + c
    if n % 19 == 0:
        print(n // 19)
