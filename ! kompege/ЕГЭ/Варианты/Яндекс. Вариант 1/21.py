def game(s1, s2, h):
    if ((h == 3) or (h == 5)) and (s1 + s2 >= 231):
        return 1
    if (h == 5) and (s1 + s2 < 231):
        return 0
    if (h < 5) and (s1 + s2 >= 231):
        return 0
    else:
        if h == 2:
            if \
                game(s1 + 4, s2, h + 1) == 1 and \
                game(s1 * 3, s2, h + 1) == 1 and \
                game(s1, s2 + 4, h + 1) == 1 and \
                game(s1, s2 * 3, h + 1) == 1:
                return 0
        if h % 2 == 0:
            return game(s1 + 4, s2, h + 1) or game(s1 * 3, s2, h + 1) or game(s1, s2 + 4, h + 1) or game(s1, s2 * 3, h + 1)
        else:
            return game(s1 + 4, s2, h + 1) and game(s1 * 3, s2, h + 1) and game(s1, s2 + 4, h + 1) and game(s1, s2 * 3, h + 1)

for i in range(1, 218):
    if game(10, i, 1) == 1:
        print(i)