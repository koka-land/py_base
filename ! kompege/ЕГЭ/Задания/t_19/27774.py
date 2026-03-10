def game(s1, s2, t):
    if (s1 + s2 >= 207) and (t == 2): return 1
    if (s1 + s2 >= 207) and (t != 2): return 0
    if (s1 + s2 < 207) and (t == 2): return 0
    if t % 2 == 0:
        return game(s1 + 1, s2, t + 1) or \
               game(s1 * 2, s2, t + 1) or \
               game(s1, s2 + 1, t + 1) or \
               game(s1, s2 * 2, t + 1)
    else:
        return game(s1 + 1, s2, t + 1) or \
               game(s1 * 2, s2, t + 1) or \
               game(s1, s2 + 1, t + 1) or \
               game(s1, s2 * 2, t + 1)

for i in range(1, 190):
    if game(17, i, 0):
        print(i)