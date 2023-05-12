'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=6393
'''

simple = []
for i in range(2, 6 * 9 + 1):
    div = 0
    for j in range(1, i + 1):
        if i % j == 0:
            div += 1
    if div == 2:
        simple.append(i)

min_sp = [10**10] * len(simple)

from itertools import product

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for j in range(2, 7):
    nums = list(product(num, repeat=j))
    for i in nums:
        sp = list(i)
        q = ''
        for qq in sp:
            q += str(qq)
        if sum(sp) in simple:
            a = int('1234' + q)
            b = (sum(sp) + 2) ** 3
            if a % b == 0:
                if a < min_sp[simple.index(sum(sp))]:
                    min_sp[simple.index(sum(sp))] = a

answer = []
for i in range(len(simple)):
    if min_sp[i] != 10**10:
        answer.append([min_sp[i], simple[i]])
answer.sort()
for i in range(len(answer)):
    print(answer[i])