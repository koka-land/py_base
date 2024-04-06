def f(start, finish):
    if start == finish:
        return 1
    elif start >= finish:
        return 0
    elif start == 43:
        return 0
    else:
        return f(start + 2, finish) + f(start + (start + 1), finish) + f(start + (start - 1), finish)

print(f(7, 63))