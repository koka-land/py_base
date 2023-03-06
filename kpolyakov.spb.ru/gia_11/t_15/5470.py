'''
https://kpolyakov.spb.ru/school/ege/gen.php?action=viewTopic&topicId=5470
'''

print('Таблица истинности')
print('P Q A F')
for P in range(2):
    for Q in range(2):
        for A in range(2):
            print (P, Q, A, (P and not(A)) <= Q)

P = set(range(254, 801))
Q = set(range(410, 824))
A = set()
k = 0

print('Решение')

for x in range(250, 830):
    if not (((x in P) and (x not in A)) <= (x in Q)):
        A.add(x)
        k += 1

print(k)