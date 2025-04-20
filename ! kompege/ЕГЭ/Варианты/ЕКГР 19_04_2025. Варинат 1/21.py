def game(s, h):
    if s >= 157 and (h == 2 or h == 4): return 1
    if s < 157 and h == 4: return 0
    if s >= 157 and h < 4: return 0
    if h % 2 == 0:
        return game(s + 2, h + 1) and game(s + 4, h + 1) and game(s * 3, h + 1)
    else:
        return game(s + 2, h + 1) or game(s + 4, h + 1) or game(s * 3, h + 1)

for s in range(1, 157):
    if game(s, 0) == 1:
        print(s)