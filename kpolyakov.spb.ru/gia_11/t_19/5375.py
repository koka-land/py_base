def game(s, h):
    if (h == 3) and (s >= 165):
        return 1
    if (h == 3) and (s < 165):
        return 0
    if (h < 3) and (s >= 165):
        return 0
    else:
        if h % 2 == 0:
            return game(s + 1, h + 1) or game(s * 2, h + 1)
        else:
            return game(s + 1, h + 1) and game(s * 2, h + 1)

for i in range(1, 165):
    if game(i, 1) == 1:
        print(i)