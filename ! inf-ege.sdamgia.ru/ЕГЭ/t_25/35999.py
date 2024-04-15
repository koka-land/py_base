'''
https://inf-ege.sdamgia.ru/problem?id=35999
*by Aldoshin Nikita
'''

for m in range(0, 31, 2):
    for n in range(1, 19, 2):
        if (200000000 <= 2**m * 3**n <= 400000000):
            print(2**m * 3**n)