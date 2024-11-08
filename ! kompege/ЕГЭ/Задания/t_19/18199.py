def game(s1, s2, h):
    if (s1 + s2 >= 77) and (h == 7):
        return 1
    if (s1 + s2 >= 77) and (h != 7):
        return 0
    if (s1 + s2 < 77) and (h == 7):
        return 0
    if h % 2 == 0:
        return game(s1 + 3, s2, h + 1) or game(s1 * 3, s2, h + 1) or game(s1, s2 + 3, h + 1) or game(s1, s2 * 3, h + 1)
    else:
        return game(s1 + 3, s2, h + 1) and game(s1 * 3, s2, h + 1) and game(s1, s2 + 3, h + 1) and game(s1, s2 * 3, h + 1)

for s2 in range(1, 65):
    if game(12, s2, 5) == 1:
        print(s2)