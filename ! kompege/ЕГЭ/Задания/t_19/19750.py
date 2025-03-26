def game(s, e, h):
    if s <= e and h == 2: return 1
    if s <= e and h != 2: return 0
    if s > 19 and h == 2: return 0
    if h % 2 != 0:
        if s % 6 == 0:
            return game(s - 5, e, h + 1) or game(s // 2, e, h + 1) or game(s // 3, e, h + 1)
        if s % 2 == 0:
            return game(s - 5, e, h + 1) or game(s // 2, e, h + 1)
        if s % 3 == 0:
            return game(s - 5, e, h + 1) or game(s // 3, e, h + 1)
        else:
            return game(s - 5, e, h + 1) or game(s + 1, e, h + 1)
    else:
        if s % 6 == 0:
            return game(s - 5, e, h + 1) and game(s // 2, e, h + 1) and game(s // 3, e, h + 1)
        if s % 2 == 0:
            return game(s - 5, e, h + 1) and game(s // 2, e, h + 1)
        if s % 3 == 0:
            return game(s - 5, e, h + 1) and game(s // 3, e, h + 1)
        else:
            return game(s - 5, e, h + 1) and game(s + 1, e, h + 1)


for s in range(20, 200):
    if game(s, 19, 0) == 1:
        print(s)
        break
