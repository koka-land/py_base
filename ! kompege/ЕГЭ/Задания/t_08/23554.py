from itertools import product

str = 'АГИЛМОРТ'
no = 'АГ'
nomer = 0

for i in product(str, repeat=5):
    word = ''.join(i)
    nomer += 1
    if word[0] not in no:
        if nomer % 2 == 0:
            if word.count('Р') >= 2:
                print(nomer)
                break


