def game(s, t, p = 0, v =  0):
    if s >= 21 and t == 5: return 1
    if s < 21 and t == 5: return 0
    if s >= 21 and t != 5: return 0
    g = []
    if t % 2 == 0:
        if p != 1: g.append(game(s + 1, t + 1, 1, v))
        if p != 2: g.append(game(s + 2, t + 1, 2, v))
        if p != 3: g.append(game(s * 2, t + 1, 3, v))
        return any(g)
    else:
        if v != 1: g.append(game(s + 1, t + 1, p, 1))
        if v != 2: g.append(game(s + 2, t + 1, p, 2))
        if v != 3: g.append(game(s * 2, t + 1, p, 3))
        return all(g)


for s in range(20, 0, -1):
    if game(s, 0) == 1:
        print(s)
        break

