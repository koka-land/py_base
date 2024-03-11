from itertools import permutations
s = 'СОВЕСТЬ'
gl = 'ОЕЬ'
sogl = 'СВТ'
slova = set()

for i in permutations(s, 7):
    slovo = ''
    for j in i:
        slovo += j
    num = slovo
    for j in gl:
        num = num.replace(j, '1')
    for j in sogl:
        num = num.replace(j, '0')
    if '00' not in num or '11' not in num:
        slova.add(slovo)

print(len(slova))
