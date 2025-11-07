from itertools import product
alph = sorted('ТВОРИЛКА')
num = 0
ans = 0

for i in product(alph, repeat=6):
    num += 1
    word = ''.join(i)
    if word == 'ВИКТОР' or word == 'КИРИЛЛ':
        ans += num

print(ans)
