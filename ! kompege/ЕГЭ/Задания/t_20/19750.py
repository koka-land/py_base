def game(s, e, h, w):
    if s <= e and h == w: return 1
    if s <= e and h != w: return 0
    if s > 19 and h == w: return 0
    if h % 2 == 0:
        if s % 6 == 0:
            return game(s - 5, e, h + 1, w) or game(s // 2, e, h + 1, w) or game(s // 3, e, h + 1, w)
        if s % 2 == 0:
            return game(s - 5, e, h + 1, w) or game(s // 2, e, h + 1, w)
        if s % 3 == 0:
            return game(s - 5, e, h + 1, w) or game(s // 3, e, h + 1, w)
        else:
            return game(s - 5, e, h + 1, w) or game(s + 1, e, h + 1, w)
    else:
        if s % 6 == 0:
            return game(s - 5, e, h + 1, w) and game(s // 2, e, h + 1) and game(s // 3, e, h + 1, w)
        if s % 2 == 0:
            return game(s - 5, e, h + 1, w) and game(s // 2, e, h + 1, w)
        if s % 3 == 0:
            return game(s - 5, e, h + 1, w) and game(s // 3, e, h + 1, w)
        else:
            return game(s - 5, e, h + 1, w) and game(s + 1, e, h + 1, w)

c = 0

for s in range(20, 100):
    if game(s, 19, 0, 3) == 1:
        if game(s, 19, 0, 1) == 0:
            c += 1
            print(s)
    if c == 2:
        break
