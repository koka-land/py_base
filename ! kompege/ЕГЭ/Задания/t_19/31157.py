def game(s1, s2, t):
    if s1 + s2 >= 171 and (t == 2): return 1
    if s1 + s2 >= 171 and t < 2: return 0
    if s1 + s2 < 171 and t == 2: return 0
    if t % 2 == 0:
        return game(s1 + 1, s2, t + 1) \
            and game(s1 * 2, s2, t + 1) \
            and game(s1, s2 + 1, t + 1) \
            and game(s1, s2 * 2, t + 1)
    else:
        return game(s1 + 1, s2, t + 1) \
            or game(s1 * 2, s2, t + 1) \
            or game(s1, s2 + 1, t + 1) \
            or game(s1, s2 * 2, t + 1)

for s2 in range(1, 146):
    if game(25, s2, 0) == 1:
        print(s2)