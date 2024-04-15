def game(s, h):
    if ((h == 3) or (h == 5)) and (s <= 12):
        return 1
    if (h == 5) and (s > 12):
        return 0
    if (h < 5) and (s <= 12):
        return 0
    else:
        if h % 2 == 0:
            return game(s // 3, h + 1) or game(s - 12, h + 1)
        else:
            return game(s // 3, h + 1) and game(s - 12, h + 1)

answer = []

for s in range(51, 200):
    if game(s, 1):
        answer.append(s)

print(len(answer))
print(answer)
