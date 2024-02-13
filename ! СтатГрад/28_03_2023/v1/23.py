def turn(x, y, z):
    if x == y:
        return 1
    if x > y:
        return 0
    else:
        if z == 0:
            return turn(x + 1, y, 1) + turn(x + 2, y, 1) + turn(x * 2, y, 2) + turn(x * 3, y, 2)
        if z == 1:
            return turn(x * 2, y, 2) + turn(x * 3, y, 2)
        else:
            return turn(x + 1, y, 1) + turn(x + 2, y, 1)

print(turn(1, 22, 0))
