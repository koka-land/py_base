def game(x, h):
    if (x >= 51) and (h == 2):
        return 1
    if (x >= 51) and (h != 2):
        return 0
    if (x < 51) and (h == 2):
        return 0
    if h % 2 == 0:
        return game(x + 1, h + 1) and game(x + 4, h + 1) and game(x * 2, h + 1)
    else:
        return game(x + 1, h + 1) or game(x + 4, h + 1) or game(x * 2, h + 1)

for s in range(1, 50):
    if game(s, 0) == 1:
        print(s)
        break