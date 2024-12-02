s = '0123456789'
for c1 in s:
    for c2 in s:
        for c3 in s:
            num = '12' + c1 + '345' + c2 + '67089' + c3
            if int(num) % 206 == 0:
                print(int(num), int(num) // 206)
