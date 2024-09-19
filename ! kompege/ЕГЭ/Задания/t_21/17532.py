def game(s1, s2, h):
    if ((h == 5) or (h == 3)) and (s1 + s2 >= 65):
        return 1
    if (h == 5) and (s1 + s2 < 65):
        return 0
    if (h != 5) and (s1 + s2 >= 65):
        return 0
    else:
        if h % 2 == 0:
            return game(s1 + 1, s2, h + 1) or game(s1 * 3, s2, h + 1) or game(s1, s2 + 1, h + 1) or game(s1, s2 * 3, h + 1)
        else:
            return game(s1 + 1, s2, h + 1) and game(s1 * 3, s2, h + 1) and game(s1, s2 + 1, h + 1) and game(s1, s2 * 3, h + 1)

for s2 in range(1, 59):
    if game(6, s2, 1) == 1:
        print(s2)