'''
https://inf-ege.sdamgia.ru/problem?id=47009
*by Aldoshin Nikita
'''


for s1 in range(61):
    for s2 in range(61):
        for s3 in range(61):
            c ='0' + s1 * '1' + s2 * '2' + s3 * '3' + '0'
            while '00' not in c:
                c = c.replace('01', '210', 1)
                c = c.replace('02', '3101', 1)
                c = c.replace('03', '2012', 1)
            if c.count('1') == 61 and c.count('2') == 50 and c.count('3') == 18:
                print(s1 + s2 + s3 + 2)
