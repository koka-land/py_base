def steps(x, nc):
    if x == 15:
        return 1
    if x > 16:
        return 0
    else:
        if nc == 1:
            return steps(x * 2, 2) + steps(x * 3, 3)
        else:
            return steps(x - 1, 1) + steps(x * 2, 2) + steps(x * 3, 3)

print(steps(3, 0))