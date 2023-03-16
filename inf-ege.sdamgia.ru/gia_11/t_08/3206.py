'''
https://inf-ege.sdamgia.ru/problem?id=3206
'''

from itertools import product
k = 0
for x in product('АКРУ', repeat = 5):
    s = ''.join(x)
    if s[0] == 'К':
        k += 1
        print(s, k)
'''
После запуска программы мы делаем вывод,что количество всех символов равно 1024,
следовательно 257 элемент это и будет слово которое начинается с буквы К
'''

