a = 3052

while a <= 10**10:
    a += 3052
    s = str(a)
    if s[0] == '1' and s[-1] == '4' and s[2:6] == '2139':
        print(a, a // 3052)
