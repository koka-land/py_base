for i in range(3013, 10**10, 3013):
    s = str(i)
    if s[0] == '1' and s[2:6] == '3948' and s[-1] == '5':
        print(i)