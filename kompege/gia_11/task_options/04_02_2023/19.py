def game(s1, s2, h):
    if (h == 3) and (s1 + s2 >= 52):
        return 1
    if (h == 3) and (s1 + s2 < 52):
        return 0
    if (h < 3) and (s1 + s2 >= 52):
        return 0
    else:
        if h % 2 == 0:
            return game(s1 + 2, s2, h + 1) or game(s1 * 3, s2, h + 1) or game(s1, s2 + 2, h + 1) or game(s1, s2 * 3, h + 1)
        else:
            return game(s1 + 2, s2, h + 1) or game(s1 * 3, s2, h + 1) or game(s1, s2 + 2, h + 1) or game(s1, s2 * 3, h + 1)

for i in range(1, 46):
    if game(5, i, 1) == 1:
        print(i)
        break