def f(x):
    if x == 141: return 1
    if x > 141: return 0
    if str(x)[-1] > str(x)[-2]:
        return f(x + 1) + f(int(f'1{str(x)[-1]}{str(x)[-2]}'))
    else:
        return f(x + 1)


print(f(100))