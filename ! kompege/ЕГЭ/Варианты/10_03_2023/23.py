def dist(st, en):
    if st == en:
        return 1
    if st < en:
        return 0
    if st > en:
        return dist(st - 2, en) + dist(st // 2, en)

print(dist(40, 10) * dist(10, 2))