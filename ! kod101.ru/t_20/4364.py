def game(s1, s2, t):
    if (s1 + s2 >= 133) and t == 3: return 1
    if (s1 + s2 < 133) and t == 3: return 0
    if (s1 + s2 >= 133) and t < 3: return 0
    if t % 2 != 0:
        return game(s1 + 4, s2, t + 1) and \
               game(s1 * 2, s2, t + 1) and \
               game(s1, s2 + 4, t + 1) and \
               game(s1, s2 * 2, t + 1)
    else:
        return game(s1 + 4, s2, t + 1) or game(s1 * 2, s2, t + 1) or game(s1, s2 + 4, t + 1) or game(s1, s2 * 2, t + 1)

for s2 in range(1, 116):
    if game(17, s2, 0) == 1:
        print(s2)