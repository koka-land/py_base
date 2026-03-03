from itertools import product
s = 'ТАРКИ'
sogl = 'ТРК'
sp = []
for i in s:
    sp.append(i)
sp.sort()

for chars_count in range(2, 20):
    number = 0
    for i in product(sp, repeat=chars_count):
        number += 1
        word = ''.join(i)
        if word[0] in sogl:
            word_only_a = word.replace('И', 'А')
            if 'ААА' in word_only_a and word_only_a.count('А') == 3:
                if number % 2 == 0:
                    break
    if number == 31314:
        print(chars_count)
        break

