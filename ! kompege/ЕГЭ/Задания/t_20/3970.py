def game(ke, t):
    if ke >= 60 and t == 3: return 1
    if ke >= 60 and t < 3: return 0
    if ke < 60 and t == 3: return 0
    if t % 2 == 0:
        return game(ke + 2, t + 1) or game(ke * 2, t + 1)
    else:
        return game(ke + 2, t + 1) and game(ke * 2, t + 1)

ans = []
for ke in range(1, 59):
    if game(ke, 0) == 1:
        ans.append(ke)
print(min(ans), max(ans))