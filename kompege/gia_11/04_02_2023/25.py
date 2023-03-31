for i in range(159, 10**7 + 1, 159):
    i = str(i)
    if i[0] == '2' and i[2] == '1' and i[-1] == '7' and i[-2] == '6':
        print(i, int(i) // 159)