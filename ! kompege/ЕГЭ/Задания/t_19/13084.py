def game(x, h):
    if x >= 84 and h == 2:
        return 1
    elif x >= 84 and h < 2:
        return 0
    elif x < 84 and h == 2:
        return 0
    else:
        if h % 2 != 0:
            if x % 2 != 0:
                return game(x + 1, h + 1) or game(x * 2, h + 1)
            else:
                return game(x + 1, h + 1) or game(x * 1.5, h + 1)
        else:
            if x % 2 != 0:
                return game(x + 1, h + 1) and game(x * 2, h + 1)
            else:
                return game(x + 1, h + 1) and game(x * 1.5, h + 1)

for s in range(1, 84):
    if game(s, 0) == 1:
        print(s)