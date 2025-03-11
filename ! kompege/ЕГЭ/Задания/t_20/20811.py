def game(x, h):
    if (x > 29) and (h == 4):
        return 1
    if (x > 29) and (h != 4):
        return 0
    if (x <= 29) and (h == 4):
        return 0
    if h % 2 == 0:
        if x % 2 == 0:
            return game(x + 4, h + 1) and game(x + 6, h + 1)
        else:
            return game(x + (x % 10), h + 1) and game(x + 6, h + 1)
    else:
        if x % 2 == 0:
            return game(x + 4, h + 1) or game(x + 6, h + 1)
        else:
            return game(x + (x % 10), h + 1) or game(x + 6, h + 1)

for s in range(1, 26):
    if game(s, 0) == 1:
        print(s)