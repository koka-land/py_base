s = '0123456789ABCDEFGHIJKLMNO'
for x in s:
    a = int('11353' + x + '12', 25)
    b = int('135' + x + '21', 25)
    if (a + b) % 24 == 0:
        print((a + b) // 24)
