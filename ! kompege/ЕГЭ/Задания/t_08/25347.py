from itertools import product
s = 'АГИНРТ'
ns = 'АГИ'
pos = 0
ans = []

for i in product(s, repeat=6):
    pos += 1
    word = ''.join(i)
    if word[0] not in ns and word.count('А') == 1 and pos % 2 != 0:
        ans.append(pos)

print(ans[0])


