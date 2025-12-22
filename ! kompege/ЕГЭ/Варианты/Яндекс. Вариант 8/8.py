from itertools import product
s = 'БАББЕБОБЬ'
count = 0

for c in product(s, repeat=7):
    slovo = ''.join(c)
    if slovo.count('Ь') <= 1:
        if 'ЕБ' not in slovo:
            if 'БЕ' not in slovo:
                count += 1

print(count)