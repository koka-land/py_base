a = int(input())
f = 0

for i in range(2, int(a ** (1 / 2)) + 1):
    if a % i == 0:
        f = 1
        break

if f == 0:
    print('Число простое')
