a = 4173

while a <= 10**10:
    a = a + 4173
    b = str(a)
    if (b[0] == '1') and (b[2] == '7') and (b[3] == '2') and (b[4] == '4') and (b[5] == '6') and (b[-1] == '1'):
        print(b, a // 4173)