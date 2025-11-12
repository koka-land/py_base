def game(s, t):
    if s <= 15 and t == 2: return 1
    if s <= 15 and t < 2: return 0
    if s > 15 and t == 2: return 0
    if t % 2 != 0:
        return game(s - 3, t + 1) or game(s - 8, t + 1) or game(s // 3, t + 1)
    else:
        return game(s - 3, t + 1) and game(s - 8, t + 1) and game(s // 3, t + 1)

for s in range(16, 200):
    if game(s, 0):
        print(s)
