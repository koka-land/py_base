for i in range(3052, 10**10 + 1, 3052):
    i = str(i)
    if i[0] == '1' and i[2:6] == '2139' and i[-1] == '4':
        print(i, int(i) // 3052)