def simple(x):
    if x <= 1: return 0
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0: return 0
    return 1

def game(s, e, t):
    if simple(s) == e and t == 2: return 1
    if simple(s) == e and t != 2: return 0
    if simple(s) != e and t == 2: return 0
    if t % 2 == 0:
        return game(s + 1, e, t + 1) and game(s + 3, e, t + 1) and game(s * 2, e, t + 1)
    else:
        return game(s + 1, e, t + 1) or game(s + 3, e, t + 1) or game(s * 2, e, t + 1)

for s in range(1, 101):
    if simple(s) == 0:
        if game(s, 1, 0) == 1:
            print(s)



