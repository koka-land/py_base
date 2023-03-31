def game(s, h):
    if (h == 4) and (s <= 12):
        return 1
    if (h == 4) and (s > 12):
        return 0
    if (h != 4) and (s <= 12):
        return 0
    else:
        if h % 2 != 0:
            return game(s // 3, h + 1) or game(s - 12, h + 1)
        else:
            return game(s // 3, h + 1) and game(s - 12, h + 1)

answer = []

for s in range(200, 12, -1):
    if game(s, 1) == 1:
        answer.append(s)

print(min(answer), max(answer))
