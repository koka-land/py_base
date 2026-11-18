d = {}

for i in range(10):
    d[f'№{str(i)}'] = 0

print(d)

from random import randint

for i in range(50):
    n = f'№{str(randint(0, 15))}'
    if n in d:
        d[n] += 1
    else:
        d[n] = 0

print(d)