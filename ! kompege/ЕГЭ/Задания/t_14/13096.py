for x in range(39):
    for y in range(39):
        a = 5 * 39**8 + \
            8 * 39**7 + \
            x * 39**6 + \
            7 * 39**5 + \
            2 * 39**4 + \
            3 * 39**3 + \
            y * 39**2 + \
            4 * 39**1 + \
            9 * 39**0
        if a % 38 == 0:
            xy = y * 39**1 + \
                 x * 39**0
            if (xy**0.5) == int(xy**0.5):
                print(x,y, a, a / 38)
