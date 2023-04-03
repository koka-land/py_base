def game():
    if (h == 2) and (s1 + s2 >= 41):
        return 1
    if (h == 2) and (s1 + s2 < 41):
        return 0
    if (h < 2) and (s1 + s2 >= 41):
        return 0
    else: