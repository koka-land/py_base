def game(s1, s2, h):
    if ((h == 3) or (h == 5)) and (s1 + s2 >= 259):
        return 1
    if (h == 5) and (s1 + s2 < 259):
        return 0
    if (h < 5) and (s1 + s2 >= 259):
        return 0
    else:
        if h % 2 == 0:
            return game(s1 + 1, s2, h + 1) or game(s1 * 2, s2, h + 1) or game(s1, s2 + 1, h + 1) or game(s1, s2 * 2, h + 1)
        else:
            return game(s1 + 1, s2, h + 1) and game(s1 * 2, s2, h + 1) and game(s1, s2 + 1, h + 1) and game(s1, s2 * 2, h + 1)

for i in range(1, 241):
    if game(17, i, 1) == 1:
        print(i)
        break