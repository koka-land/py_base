audio = 2 * 56000 *15 * (27 * 60 + 27)

for name in range(1, 10**10):
    if (audio + name * 8 * 1024 * 28) / 367217732 > 332:
        print(name)
        break