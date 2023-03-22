for i in range(9601, 10**10, 9601):
    s = str(i)
    if s[0:2:] == '19' and s[-1] == '9' and '105' in s:
        print(i, i // 9601)