for i in range(98591, 10**12, 98591):
    a = str(i)
    if a[0:2] == '12' and a[3] == '3' and a[-1] == '9' and a[-6:-3] == '456':
        print(i, i // 98591)
