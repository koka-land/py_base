def g(s1, s2, t):
    if (s1 + s2) >= 154 and t == 2: return 1
    if (s1 + s2) < 154 and t == 2: return 0
    if (s1 + s2) >= 154 and t != 2: return 0
    if t % 2 == 0:
        return g(s1 + 4, s2, t + 1) or \
               g(s1 * 3, s2, t + 1) or \
               g(s1, s2 + 4, t + 1) or \
               g(s1, s2 * 3, t + 1)
    else:
        return g(s1 + 4, s2, t + 1) or \
               g(s1 * 3, s2, t + 1) or \
               g(s1, s2 + 4, t + 1) or \
               g(s1, s2 * 3, t + 1)

for s in range(1, 143):
    if g(11, s, 0) == 1:
        print(s)