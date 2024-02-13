for n in range(100):
    if n % 100 >= 10 and n % 100 < 20 or n % 10 > 4 or n % 10 == 0:
        print(n, 'примеров')
    elif n % 10 == 1:
        print(n, 'пример')
    else:
        print(n, 'примерa')