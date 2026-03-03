from itertools import product
s = 'АЖИМНУЧ'
n = 0
answer = 0

for i in product(s, repeat=6):
    n += 1
    word = ''.join(i)
    if word[0] != 'Ж' and word.count('Ч') <= 1 and n % 2 == 0:
        answer += 1

print(answer)


