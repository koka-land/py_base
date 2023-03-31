for i in range(21, 10**8, 21):
    s = str(i)
    if s[0:4] == '1234' and s[-2::] == '54':
        print(i, i // 21)