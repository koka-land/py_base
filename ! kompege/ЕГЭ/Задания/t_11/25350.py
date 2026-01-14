for i in range(2, 50):
    if (((i * 105) / 8) * 65536) / 1024**2 >= 7:
        print(2**(i - 1) + 1)
        break