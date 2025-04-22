from itertools import product

s = 'АКЛПШЮ'
n = 0

for i in product(s, repeat=6):
    slovo = ''.join(i)
    n += 1
    if len(set(slovo)) == 6 and slovo[0] != 'А' and n % 2 != 0:
        print(n)
        break
