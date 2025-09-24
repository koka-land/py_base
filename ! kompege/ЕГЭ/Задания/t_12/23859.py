for i in range(1, 501):
    sum1 = i + ((1000 - 2 * i) * 2)
    sum2 = i + (i * 2)
    raz = sum1 - sum2
    if raz == 200:
        print(1000 - 2 * i)