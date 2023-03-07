a = 159

while a <= 10 ** 7:
    a = a + 159
    b = str(a)
    if (b[0] == '2') and (b[2] == '1') and (b[-2] == '6') and (b[-1] == '7'):
        print(b, a // 159)
