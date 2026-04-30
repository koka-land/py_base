for x in range(-100, 100):
    a = (not(x < 15))
    b = (x > 12)
    c = (x <= 3)
    f = a or b or c
    if f == 0:
        print(x)
