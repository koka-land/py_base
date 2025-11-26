def game(s, t, p):
    if s >= 231: return t % 2 == 0
    if t == 0: return 0
    if p == 1:
        h = [game(s + 3, t - 1, 2), game(s * 3, t - 1, 2)]
    else:
        h = [game(s + 5, t - 1, 1), game(s * 3, t - 1, 1)]
    return any(h) if t % 2 else all(h)

print([i for i in range(10, 121) if game(i, 2, 1)])
print([i for i in range(10, 121) if game(i, 3, 1) and (not(game(i, 1, 1)))])
print([i for i in range(10, 121) if game(i, 4, 1) and (not(game(i, 2, 1)))])
