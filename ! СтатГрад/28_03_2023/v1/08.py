from itertools import product

s = 'МИТРОФАН'
sog = 'МТРФН'
gl = 'ИОА'
ans = 0

error = ['ИО', 'ОИ', 'ИА', 'АИ', 'ОА', 'АО']

for i in product(s, repeat=6):
    er = 0
    gl_count = 0
    slovo = ''.join(i)
    for j in s:
        if slovo.count(j) > 1:
            er = 1
            break
    if er == 0:
        for j in gl:
            gl_count += slovo.count(j)
        if gl_count <= 2:
            er = 0
            for j in error:
                if j in slovo:
                    er = 1
                    break
            if er == 0:
                ans += 1

print(ans)