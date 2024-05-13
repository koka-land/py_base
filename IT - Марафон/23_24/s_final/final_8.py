num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
prime = []
a = input().split()

for p in range(2, 1500):
    pr = True
    for i in range(2, int(p ** 0.5 + 1)):
        if p % i == 0:
            pr = False
            break
    if pr:
        prime.append(p)

f = 0
for i in a:
    if i not in num:
        f = 1
        break
if f == 1 or len(a) != 3:
    print('Wrong input')
else:
    b = ''
    for i in a:
        b += str(num.index(i))
    b = int(b)
    if b in prime:
        print(b)
    else:
        bl = 10 ** 10
        for i in prime:
            if abs(b - i) < abs(b - bl):
                bl = i
    print(bl)