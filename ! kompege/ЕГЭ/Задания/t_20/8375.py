def game(s1, s2, e, h):
    if (s1 < 10 or s2 < 10) and h == 3: return 1
    if (s1 < 10 or s2 < 10) and h != 3: return 0
    if (s1 >= 10 and s2 >= 10) and h == 3: return 0
    if h % 2 != 0:
        return game(s1 - 1, s2, e, h + 1) and \
               game(s1 - 3, s2, e, h + 1) and \
               game(s1, s2 - 1, e, h + 1) and \
               game(s1, s2 - 3, e, h + 1)
    else:
        return game(s1 - 1, s2, e, h + 1) or \
               game(s1 - 3, s2, e, h + 1) or \
               game(s1, s2 - 1, e, h + 1) or \
               game(s1, s2 - 3, e, h + 1)

for s in range(10, 100):
    if game(13, s, 10, 0) == 1:
        print(s)
