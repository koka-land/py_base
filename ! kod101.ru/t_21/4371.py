def game(s, e, t):
    if s >= e and (t == 2 or t == 4): return 1
    if s >= e and t != 4: return 0
    if s < e and t == 4: return 0
    if t % 2 == 0:
        return game(s + 5, e, t + 1) and game(s * 3, e, t + 1)
    else:
        return game(s + 5, e, t + 1) or game(s * 3, e, t + 1)

for s in range(1, 151):
    if game(s, 4 * s, 0) == 1:
        print(s)