import math
ans = []

for i in range(2, 50):
    if ((math.ceil((i * 1234) / 8)) * 12345678) / 1024**3 >= 12:
        print(max(ans))
        break
    else:
        ans.append(2 ** i)

