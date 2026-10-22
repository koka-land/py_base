def game(s, w, t):
    if s >= w and t == 2: return 1
    if s >= w and t < 2: return 0
    if s < w and t == 2: return 0
    if t % 2 == 0:
        return game(s + 5, w, t + 1) and game(s * 3, w, t + 1)
    else:
        return game(s + 5, w, t + 1) or game(s * 3, w, t + 1)

sp = []
for s in range(1, 151):
    if game(s, s * 4, 0) == 1:
        sp.append(s)

print(len(sp))