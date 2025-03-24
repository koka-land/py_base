def v7(x):
    s = ''
    while x > 0:
        s = str(x % 7) + s
        x //= 7
    return(s)

ans = [i for i in range(2030) if v7(7**170 + 7**100 - i).count('0') == 71]

print(max(ans))