ans = []
def div(x):
    sp = []
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            sp.append(i)
            sp.append(x // i)
    sp.sort()
    for i in sp:
        if i % 10 == 5 and i != 5 and i != x:
            return(i)
    return(0)


for i in range(902714, 10**10):
    a = 0
    if len(ans) == 6:
        break
    a = div(i)
    if a > 0:
        ans.append([i, a])

print(ans)
