from itertools import product

s = 'АКЛСУ'

for k_b in range(2, 20):
    n = 0
    last_n = 0
    for i in product(s, repeat=k_b):
        n += 1
        word_original = ''.join(i)
        word_only_a = word_original.replace('У', 'А')
        if n % 2 == 0:
            if word_original[0] == 'Л' or word_original[0] == 'С':
                if word_only_a.count('А') <= 2:
                    if 'АА' not in word_only_a:
                        last_n = n

    if last_n == 12368:
        print(k_b)
        break