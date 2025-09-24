from itertools import product

s = 'АКОРСТ'
s1 = 'АСТ'
n = 0

for i in product(s, repeat=5):
    n += 1
    word = ''.join(i)
    if (word[0] not in s1) and (word.count('О') == 2) and (n % 2 == 0):
        ans = n

print(ans)